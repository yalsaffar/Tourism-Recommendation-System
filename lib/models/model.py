import sys
from statistics import mean

# Add a path to sys.path
sys.path.append('../datasets')
from flights import  flights_reco
from userdata import users
from data_structure import data_strcture
from Ranges import Ranges
import numpy as np
import pandas as pd
from Airbnb_reco import Airbnb_reco
from Places_reco import Places_reco

import warnings
warnings.filterwarnings("ignore")




#titles,indices, cosine_sim, df = model_computations()
def clf( UserId,user_df, pool_df,cosine_sim,location,previous='ALC'):
    """
    Takes in user preferences, user and pool dataframes, and precomputed cosine similarity matrix, and returns
    a recommended flight.

    Args:
        UserId (int): ID of the user.
        user_df (pandas.DataFrame): DataFrame containing user information and preferences.
        pool_df (pandas.DataFrame): DataFrame containing information about flights in the pool.
        cosine_sim (numpy.ndarray): Precomputed cosine similarity matrix.
        location (str): Name of the city the user is interested in traveling to.
        previous (str, optional): The previous location the user visited. Defaults to 'ALC'.

    Returns:
        pandas.DataFrame: The recommended flight.
    """

    #titles,indices, cosine_sim, df = model_computations()
    titles = pd.read_csv('/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/titles.csv')
    df = pd.read_csv('/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/df.csv')
    df2 = df.reset_index()
    titles = pd.Series(df2['Description'])
    indices = pd.Series(df2.index, index = df2['Description'])
    #cosine_sim = np.load('../datasets/data_files/cosine_sim.npy')
    #user_df = user_df[user_df['UserId'] == UserId]
    
    #_, user_df, pool_df = data_strcture()


    def Flights_Reco(location, previous,best):
        
        recos = flights_reco(location,previous,best,titles,indices, cosine_sim,df)
        return recos.head(50)

    price_ranges, time_cols_dict, cities_dict, price_ranges_air, beds_ranges, people_ranges, reviews_ranges = Ranges()
    

    
    location = cities_dict[location]
    city_names = list(set(df['cityTo'])) 
    city_counts = user_df.filter(items=city_names).sum().sort_values(ascending=False)

    highest_city = city_counts.index[0]

    price_max_col = user_df.filter(regex=r'^PriceLvl_(?!.*airbnb)').idxmax(axis=1)


    activity_max_col = user_df.filter(['Beach', 'Nature', 'Cultural', 'Historical', 'Adventurous']).idxmax(axis=1)
    time_max_col = user_df.filter(['EarlyMorning', 'Morning', 'Noon', 'Afternoon', 'Evening', 'Night']).idxmax(axis=1)
    
    reco = Flights_Reco(location,previous,cities_dict[highest_city])
    reco['local_departure'] = pd.to_datetime(reco['local_departure'])

    reco_filtered = reco[(reco['price'] >= price_ranges[str(price_max_col[0])][0]) & (reco['price'] <= price_ranges[str(price_max_col[0])][1])]
    reco_filtered2 = reco_filtered[(reco_filtered['local_departure'].dt.hour >= time_cols_dict[str(time_max_col[0])][0]) & (reco_filtered['local_departure'].dt.hour <= time_cols_dict[str(time_max_col[0])][1])]
    reco_filtered3 = reco_filtered2[reco_filtered2['category']== str(activity_max_col[0])]

    reco_others = reco[(reco['price'] < price_ranges[str(price_max_col[0])][0]) | (reco['price'] > price_ranges[str(price_max_col[0])][1])]
    reco_others2 = reco_filtered[(reco_filtered['local_departure'].dt.hour < time_cols_dict[str(time_max_col[0])][0]) | (reco_filtered['local_departure'].dt.hour > time_cols_dict[str(time_max_col[0])][1])]
    reco_others3 = reco_filtered2[reco_filtered2['category']!= str(activity_max_col[0])]

    reco_final = pd.concat([reco_filtered,reco_filtered2,reco_filtered3, reco_others,reco_others2,reco_others3])
    reco_final = reco_final.drop_duplicates(keep='first')
    cities = ['MAD','BCN','AGP','MAH','SVQ','GRO']
    reco_final = reco_final[reco_final['flyTo'].isin(cities)]
    #print(reco_final)
    previous = reco_final['flyTo'].iloc[0]
    print("Flights Reco....")
    #print("Do you like this offer: (yes:1, no:0)")
    #indicator = input()
    #print( reco_final['cityTo'].iloc[0], reco_final['category'].iloc[0], reco_final['price'].iloc[0], str(reco_final['local_departure'].iloc[0]), indicator)
    
    #pool_df, updated_user_df = users(0 ,df, user_df, pool_df, reco_final['cityTo'].iloc[0], reco_final['category'].iloc[0], reco_final['price'].iloc[0], str(reco_final['local_departure'].iloc[0]), int(indicator))
    #user_df = updated_user_df.copy()
    City = reco_final['cityTo'].iloc[0]
    Category = reco_final['category'].iloc[0]
    Price_flight =  reco_final['price'].iloc[0]
    time =  str(reco_final['local_departure'].iloc[0])
    
    return reco_final.iloc[0], City, Category, Price_flight, time
#------------------------------------------------------------
def Rent_Reco(location,previous,best_price,best_beds,best_People,best_reviews):
    titles = pd.read_csv('/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/titles_air.csv')
    df = pd.read_csv('/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/airbnb_clean.csv')
    df2 = df.reset_index()
    titles = pd.Series(df2['Text'])
    indices = pd.Series(df2.index, index = df2['Text'])
    cosine_sim = np.load('../datasets/data_files/cosine_sim_air.npy')
    recos = Airbnb_reco(location,previous,best_price,best_beds,best_People,best_reviews,titles,indices, cosine_sim, df)
    return recos.head(50)
        
def clf_Airbnb(UserId,user_df,pool_df,df,City,Price_flight,Category,time,prev = 50059918):
    """
    Given the user inputs, returns a list of recommended Airbnb rentals.

    Args:
        UserId (int): User identification number
        user_df (pandas.DataFrame): User dataframe containing the user preferences
        pool_df (pandas.DataFrame): Pool of recommended rentals
        df (pandas.DataFrame): Airbnb dataframe containing the listings data
        City (str): City for which the rentals are being recommended
        Price_flight (float): Flight price for the city
        Category (str): Category of activities preferred by the user
        time (str): Time of flight departure
        prev (int, optional): Index of previous city visited by the user. Defaults to 50059918.

    Returns:
        tuple: Returns a tuple containing the updated pool of recommended rentals, updated user dataframe, recommended rental, recommended city, recommended category, flight price, time of flight departure, price of recommended rental, number of beds of recommended rental, number of people accomodated in recommended rental, number of reviews of recommended rental
    """

    price_ranges, time_cols_dict, cities_dict, price_ranges_air, beds_ranges, people_ranges, reviews_ranges = Ranges()
    if City == 'Málaga':
        City = 'Malaga'
    #City = 'Madrid' #inputed
    #prev = 50059918 # recursive
    #price_flight = 200 #inputed
    #category = 'Historical' #inputed
    #time = '2023-04-15 14:30:45' #inputed

    #-------------------------
    price_max_air = user_df[user_df['UserId'] == UserId].filter(regex='PriceLvl.*airbnb').idxmax(axis=1)
    beds_max_air = user_df[user_df['UserId']==UserId].filter(like='Beds_').idxmax(axis=1)
    people_max_air = user_df[user_df['UserId']==UserId].filter(like='People_').idxmax(axis=1)
    reviews_max_air = user_df[user_df['UserId']==UserId].filter(like='Reviews_').idxmax(axis=1)

    best_price_air = mean(price_ranges_air[str(price_max_air)[5:-14]])
    best_beds_air = mean(beds_ranges[str(beds_max_air)[5:-14]])
    best_people_air = mean(people_ranges[str(people_max_air)[5:-14]])
    best_reviews_air = mean(reviews_ranges[str(reviews_max_air)[5:-14]])
    # ---------------------------
    #print(City,prev, best_price_air,best_beds_air,best_people_air, best_reviews_air)
    print("Airbnb Reco....")

    reco = Rent_Reco(City,prev, best_price_air,best_beds_air,best_people_air, best_reviews_air)
    #r = Airbnb_reco('Malaga',50059918,200,10,2,100,titles,indices, cosine_sim, df)


    reco = reco.sort_values(['fear', 'anger', 'negative', 'sadness', 'disgust',]).sort_values([ 'number_of_reviews','trust', 'surprise','positive',  'joy'],ascending=False)
    reco = reco.head(10)
    #print(reco['listing_url'].iloc[0])
    #print("Do you like this offer? 1 for yes, 0 for no")
    #indicator = input()
    #pool_df, updated_user_df = users(UserId ,df, user_df, pool_df, reco['City'].iloc[0], category, price_flight,reco['price'].iloc[0],reco['beds'].iloc[0],reco['People'].iloc[0],reco['number_of_reviews'].iloc[0], time, int(indicator))
    #user_df = updated_user_df.copy()
    City= reco['City'].iloc[0]
    Price_Air = reco['price'].iloc[0]
    Beds_air = reco['beds'].iloc[0]
    People_air = reco['People'].iloc[0]
    Reviews_air = reco['number_of_reviews'].iloc[0]
    
    return pool_df, user_df, reco.iloc[0], City, Category, Price_flight, time, Price_Air,Beds_air,People_air,Reviews_air
def place_recommendation(user_df, user_id, prev_place_id, filtered_df):
    """
    This function recommends a place to visit based on the user's preferences.

    Parameters:
    user_df (pandas.DataFrame): User DataFrame containing the user's preferences.
    user_id (int): User ID for the user whose preferences we want to use.
    prev_place_id (int or None): ID of the previously recommended place. If None, no previous recommendation exists.
    filtered_df (pandas.DataFrame): DataFrame containing filtered places based on user's flights and Airbnb recommendations.

    Returns:
    pandas.DataFrame: DataFrame containing the recommended place.
    """

    #print(user_df['place_morning'])
    #print(user_df.columns)
    print("Places Reco....")


    #print(user_df.filter(['place_morning', 'place_afternoon', 'place_night']))
    time_max_col = user_df.filter(['place_morning', 'place_afternoon', 'place_night']).idxmax(axis=1)
    category_max_col = user_df.filter(['place_historical', 'place_nature', 'place_cultural', 'place_adventurous', 'place_beach']).idxmax(axis=1)

    preferred_time = str(time_max_col[user_id])
    preferred_category = str(category_max_col[user_id])

    df_filtered = filtered_df[(filtered_df['category'] == preferred_category) & (filtered_df['time_of_day'] == preferred_time)]

    if prev_place_id is not None:
        df_filtered = df_filtered[df_filtered['place_id'] != prev_place_id]

    if not df_filtered.empty:
        recommended_place = df_filtered.sample()
        return recommended_place
    else:
        # If no place matches the preferred time and category, recommend a random place in the city
        df_city = filtered_df
        if prev_place_id is not None:
            df_city = df_city[df_city['place_id'] != prev_place_id]
        recommended_place = df_city.sample()
        return recommended_place

def clf_places(City,UserId,user_df,previous = 712):
    """
    Uses cosine similarity to recommend a place/activity based on user's preferred city.

    Args:
    - City (str): The name of the city for which the activity is recommended.
    - UserId (int): The ID of the user for which the recommendation is made.
    - user_df (pd.DataFrame): The DataFrame containing user preferences.
    - previous (int): The ID of the previous recommended place/activity.

    Returns:
    - recommended_place (pd.Series): A pandas series containing information about the recommended place/activity.
    - recommended_place['category'] (str): The category of the recommended place/activity.
    - recommended_place['time_of_day'] (str): The time of day when the recommended place/activity is best suited.
    """

    if City == 'Málaga':
        City = 'Malaga'
    #places_titles = pd.read_csv('../datasets/data_files/Titles_Places.csv')
    #places_indices = pd.read_csv('../datasets/data_files/Indices_Places.csv')
    places_cosine_sim = np.load('/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/Cosine_Similarity_Places.npy')
    places_df = pd.read_csv('/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/places_activities_spain_final.csv')
    recos = Places_reco(City, places_cosine_sim, places_df, previous)
    recommended_place = place_recommendation(user_df, UserId, previous, recos)
    recommended_place = recommended_place.reset_index()
    return recommended_place, recommended_place['category'][0],recommended_place['time_of_day'][0]
#['category'][1]

