from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flights import flights_reco
from userdata import users
from data_structure import data_strcture
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

titles = pd.read_csv('titles.csv')
df = pd.read_csv('df.csv')
df2 = df.reset_index()
titles = pd.Series(df2['Description'])
indices = pd.Series(df2.index, index=df2['Description'])
cosine_sim = np.load('cosine_sim.npy')
app = Flask(__name__)
socketio = SocketIO(app)
_, user_df, pool_df = data_strcture()
def model(location, previous, best):
    recos = flights_reco(location, previous, best, titles, indices, cosine_sim, df)
    return recos.head(50)
price_ranges = {'PriceLvl_1': [0, 100], 'PriceLvl_2': [100, 200], 'PriceLvl_3': [200, 300], 'PriceLvl_4': [300, 400],
                'PriceLvl_5': [400, 500], 'PriceLvl_6': [500, 600], 'PriceLvl_7': [600, 700], 'PriceLvl_8': [700, 800],
                'PriceLvl_9': [800, 900], 'PriceLvl_10': [900, 1000], 'PriceLvl_15': [1000, 1500],
                'PriceLvl_20': [1500, 2000], 'PriceLvl_30': [2000, 3000], 'PriceLvl_40': [3000, 4000]}

time_cols_dict = {
    'EarlyMorning': [4, 7],
    'Morning': [7, 12],
    'Noon': [12, 16],
    'Afternoon': [16, 19],
    'Evening': [19, 23],
    'Night': [0, 4]
}

cities_dict = {'Tirana': 'TIA',
 'Graz': 'GRZ',
 'Innsbruck': 'INN',
 'Brussels': 'CRL',
 'Paphos': 'PFO',
 'Tallinn': 'TLL',
 'Helsinki': 'HEL',
 'Turku': 'TKU',
 'Lille': 'LIL',
 'Lyon': 'LYS',
 'Paris': 'ORY',
 'Kutaisi': 'KUT',
 'Dresden': 'DRS',
 'Leipzig': 'LEJ',
 'Munich': 'MUC',
 'Athens': 'ATH',
 'Chania': 'CHQ',
 'Santorini': 'JTR',
 'Thessaloniki': 'SKG',
 'Knock, County Mayo': 'NOC',
 'County Kerry': 'KIR',
 'Cagliari': 'CAG',
 'Catania': 'CTA',
 'Naples': 'NAP',
 'Olbia': 'OLB',
 'Trapani': 'TPS',
 'Venice': 'TSF',
 'Kaunas': 'KUN',
 'Vilnius': 'VNO',
 'Oslo': 'TRF',
 'Stavanger': 'SVG',
 'Warsaw': 'WMI',
 'Timișoara': 'TSR',
 'Niš': 'INI',
 'Málaga': 'AGP',
 'Alicante': 'ALC',
 'Almería': 'LEI',
 'Asturias': 'OVD',
 'Bilbao': 'BIO',
 'Barcelona': 'BCN',
 'Badajoz': 'BJZ',
 'Béziers': 'BZR',
 'Brindisi': 'BDS',
 'Donostia / San Sebastián': 'EAS',
 'Fuerteventura': 'FUE',
 'Girona': 'GRO',
 'Granada': 'GRX',
 'Ibiza': 'IBZ',
 'Jerez de la Frontera': 'XRY',
 'A Coruña': 'LCG',
 'Lanzarote': 'ACE',
 'Madrid': 'MAD',
 'Agadir': 'AGA',
 'Menorca': 'MAH',
 'Melilla': 'MLN',
 'Palma, Majorca': 'PMI',
 'Pamplona': 'PNA',
 'Santander': 'SDR',
 'Seville': 'SVQ',
 'Tenerife': 'TFS',
 'Valencia': 'VLC',
 'Valladolid': 'VLL',
 'Vigo': 'VGO',
 'Vitoria-Gasteiz': 'VIT',
 'Valverde': 'VDE',
 'Zaragoza': 'ZAZ',
 'Santiago de Compostela': 'SCQ'}
# Load flight data into a pandas dataframe
flight_data = pd.read_csv('Flights.csv')
values=1
@socketio.on('swipe')
def swipe():
    data = request.get_json()
    global values
    value=data['value']
    if value == 1:
        reco(1)
    else:
        reco(0)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/reco',methods=['POST'])
def rec():
    _, user_df, pool_df = data_strcture()
    if request.method == 'POST':

        # Get user preferences from the form
        flyFrom = request.form['city']

        # Filter flights based on user preferences
        previous = flyFrom

        for i in range(10):
            location = flyFrom
            city_names = list(set(df['cityTo']))  # Replace with your desired cities
            city_counts = user_df.filter(items=city_names).sum().sort_values(ascending=False)

            highest_city = city_counts.index[0]
            second_highest_city = city_counts.index[1]
            third_highest_city = city_counts.index[2]

            price_max_col = user_df.filter(like='PriceLvl_').idxmax(axis=1)
            activity_max_col = user_df.filter(['Beach', 'Nature', 'Cultural', 'Historical', 'Adventurous']).idxmax(
                axis=1)
            time_max_col = user_df.filter(['EarlyMorning', 'Morning', 'Noon', 'Afternoon', 'Evening', 'Night']).idxmax(
                axis=1)

            if i <= 4:
                reco = model(location, previous, cities_dict[second_highest_city])
            elif i <= 8:
                reco = model(location, previous, cities_dict[third_highest_city])
            else:
                reco = model(location, previous, cities_dict[highest_city])
            reco['local_departure'] = pd.to_datetime(reco['local_departure'])

            reco_filtered = reco[(reco['price'] >= price_ranges[str(price_max_col[0])][0]) & (
                    reco['price'] <= price_ranges[str(price_max_col[0])][1])]
            reco_filtered2 = reco_filtered[
                (reco_filtered['local_departure'].dt.hour >= time_cols_dict[str(time_max_col[0])][0]) & (
                        reco_filtered['local_departure'].dt.hour <= time_cols_dict[str(time_max_col[0])][1])]
            reco_filtered3 = reco_filtered2[reco_filtered2['category'] == str(activity_max_col[0])]

            reco_others = reco[(reco['price'] < price_ranges[str(price_max_col[0])][0]) | (
                    reco['price'] > price_ranges[str(price_max_col[0])][1])]
            reco_others2 = reco_filtered[
                (reco_filtered['local_departure'].dt.hour < time_cols_dict[str(time_max_col[0])][0]) | (
                        reco_filtered['local_departure'].dt.hour > time_cols_dict[str(time_max_col[0])][1])]
            reco_others3 = reco_filtered2[reco_filtered2['category'] != str(activity_max_col[0])]

            reco_final = pd.concat(
                [reco_filtered, reco_filtered2, reco_filtered3, reco_others, reco_others2, reco_others3])
            reco_final = reco_final.drop_duplicates(keep='first')

            previous = reco_final['flyTo'].iloc[0]
            pool_df, user_df = users(0, df, user_df, pool_df, reco_final['cityTo'].iloc[0],
                                     reco_final['category'].iloc[0],
                                     reco_final['price'].iloc[0], str(reco_final['local_departure'].iloc[0]),
                                     1)
            reco_final = reco_final.tail(15)
            recommendations = []
            for _, row in reco_final.iterrows():
                recommendation = (flyFrom, row['flyTo'], row['price'])
                recommendations.append(recommendation)
        return render_template('recommendations.html', recommendations=recommendations)

def reco(value):

    _, user_df, pool_df = data_strcture()
    if request.method == 'POST':

        # Get user preferences from the form
        flyFrom = request.form['city']

        # Filter flights based on user preferences
        previous = flyFrom

        for i in range(10):
            location = flyFrom
            city_names = list(set(df['cityTo']))  # Replace with your desired cities
            city_counts = user_df.filter(items=city_names).sum().sort_values(ascending=False)

            highest_city = city_counts.index[0]
            second_highest_city = city_counts.index[1]
            third_highest_city = city_counts.index[2]

            price_max_col = user_df.filter(like='PriceLvl_').idxmax(axis=1)
            activity_max_col = user_df.filter(['Beach', 'Nature', 'Cultural', 'Historical', 'Adventurous']).idxmax(
                axis=1)
            time_max_col = user_df.filter(['EarlyMorning', 'Morning', 'Noon', 'Afternoon', 'Evening', 'Night']).idxmax(
                axis=1)

            if i <= 4:
                reco = model(location, previous, cities_dict[second_highest_city])
            elif i <= 8:
                reco = model(location, previous, cities_dict[third_highest_city])
            else:
                reco = model(location, previous, cities_dict[highest_city])
            reco['local_departure'] = pd.to_datetime(reco['local_departure'])

            reco_filtered = reco[(reco['price'] >= price_ranges[str(price_max_col[0])][0]) & (
                    reco['price'] <= price_ranges[str(price_max_col[0])][1])]
            reco_filtered2 = reco_filtered[
                (reco_filtered['local_departure'].dt.hour >= time_cols_dict[str(time_max_col[0])][0]) & (
                        reco_filtered['local_departure'].dt.hour <= time_cols_dict[str(time_max_col[0])][1])]
            reco_filtered3 = reco_filtered2[reco_filtered2['category'] == str(activity_max_col[0])]

            reco_others = reco[(reco['price'] < price_ranges[str(price_max_col[0])][0]) | (
                    reco['price'] > price_ranges[str(price_max_col[0])][1])]
            reco_others2 = reco_filtered[
                (reco_filtered['local_departure'].dt.hour < time_cols_dict[str(time_max_col[0])][0]) | (
                        reco_filtered['local_departure'].dt.hour > time_cols_dict[str(time_max_col[0])][1])]
            reco_others3 = reco_filtered2[reco_filtered2['category'] != str(activity_max_col[0])]

            reco_final = pd.concat(
                [reco_filtered, reco_filtered2, reco_filtered3, reco_others, reco_others2, reco_others3])
            reco_final = reco_final.drop_duplicates(keep='first')

            previous = reco_final['flyTo'].iloc[0]
            pool_df, user_df = users(0, df, user_df, pool_df, reco_final['cityTo'].iloc[0],
                                     reco_final['category'].iloc[0],
                                     reco_final['price'].iloc[0], str(reco_final['local_departure'].iloc[0]),
                                     value)
            reco_final=reco_final.tail(15)
            recommendations = []
            for _, row in reco_final.iterrows():
                recommendation = (flyFrom, row['flyTo'], row['price'])
                recommendations.append(recommendation)
        return render_template('recommendations.html', recommendations=recommendations)


if __name__ == '__main__':
    socketio.run(app)
