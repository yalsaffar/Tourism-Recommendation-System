import sys
import os
import pandas as pd
import numpy as np
os.chdir('../lib')
sys.path.append('../lib/datasets')
sys.path.append('../lib/models')
## /datasets imports
from Flights import flights_dataset
from Airbnb_data import Airbnb_data
from data_structure import data_strcture
from Ranges import Ranges
from userdata import users
## /models imports
from Airbnb_reco import Airbnb_reco
from flights import flights_reco
from model import clf, clf_Airbnb
from Places_reco import Places_reco



# Library

## datasets –-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------

def test_Airbnb_data():
    test_col = ['id',
    'listing_url',
    'description',
    'host_is_superhost',
    'neighbourhood_cleansed',
    'latitude',
    'longitude',
    'property_type',
    'room_type',
    'accommodates',
    'bathrooms_text',
    'beds',
    'amenities',
    'price',
    'minimum_nights',
    'maximum_nights',
    'minimum_minimum_nights',
    'maximum_minimum_nights',
    'minimum_maximum_nights',
    'maximum_maximum_nights',
    'has_availability',
    'number_of_reviews',
    'instant_bookable',
    'City',
    'comments',
    'Text',
    'People',
    'Min_Duration',
    'fear',
    'anger',
    'anticip',
    'trust',
    'surprise',
    'positive',
    'negative',
    'sadness',
    'disgust',
    'joy']
    assert list(Airbnb_data().columns) == test_col

def test_data_structure():
    assert len(data_strcture()) == 3

    test_df_col = ['flyFrom', 'flyTo', 'price', 'cityFrom', 'cityTo', 'countryFrom',
       'distance', 'duration', 'local_departure', 'category']
    assert list(data_strcture()[0].columns) == test_df_col

    test_user_col = ['PriceLvl_1',
    'PriceLvl_2',
    'PriceLvl_3',
    'PriceLvl_4',
    'PriceLvl_5',
    'PriceLvl_6',
    'PriceLvl_7',
    'PriceLvl_8',
    'PriceLvl_9',
    'PriceLvl_10',
    'PriceLvl_15',
    'PriceLvl_20',
    'PriceLvl_30',
    'PriceLvl_40',
    'PriceLvl_1_airbnb',
    'PriceLvl_2_airbnb',
    'PriceLvl_3_airbnb',
    'PriceLvl_4_airbnb',
    'PriceLvl_5_airbnb',
    'PriceLvl_6_airbnb',
    'PriceLvl_7_airbnb',
    'PriceLvl_8_airbnb',
    'PriceLvl_9_airbnb',
    'PriceLvl_10_airbnb',
    'PriceLvl_15_airbnb',
    'Beds_1_airbnb',
    'Beds_2_airbnb',
    'Beds_3_airbnb',
    'Beds_4_airbnb',
    'Beds_5_airbnb',
    'Beds_6_airbnb',
    'Beds_7_airbnb',
    'Beds_8_airbnb',
    'Beds_9_airbnb',
    'Beds_10_airbnb',
    'People_1_airbnb',
    'People_2_airbnb',
    'People_3_airbnb',
    'People_4_airbnb',
    'People_5_airbnb',
    'People_6_airbnb',
    'People_7_airbnb',
    'People_8_airbnb',
    'People_9_airbnb',
    'People_10_airbnb',
    'People_15_airbnb',
    'Reviews_1_airbnb',
    'Reviews_2_airbnb',
    'Reviews_3_airbnb',
    'Reviews_4_airbnb',
    'Reviews_5_airbnb',
    'Beach',
    'Nature',
    'Cultural',
    'Historical',
    'Adventurous',
    'UserId',
    'EarlyMorning',
    'Morning',
    'Noon',
    'Afternoon',
    'Evening',
    'Night',
    'A Coruña',
    'Agadir',
    'Alicante',
    'Almería',
    'Asturias',
    'Badajoz',
    'Barcelona',
    'Bilbao',
    'Brindisi',
    'Béziers',
    'Donostia / San Sebastián',
    'Fuerteventura',
    'Girona',
    'Granada',
    'Ibiza',
    'Jerez de la Frontera',
    'Lanzarote',
    'Madrid',
    'Melilla',
    'Menorca',
    'Málaga',
    'Palma, Majorca',
    'Pamplona',
    'Santander',
    'Santiago de Compostela',
    'Seville',
    'Tenerife',
    'Valencia',
    'Valladolid',
    'Valverde',
    'Vigo',
    'Vitoria-Gasteiz',
    'Zaragoza']
    assert list(data_strcture()[1].columns) == test_user_col
    assert len(data_strcture()[1].columns) == 96
        
    test_pool_col = ['inptCity',
    'inptTime',
    'inptCat',
    'inptPrice',
    'PriceLvl_1',
    'PriceLvl_2',
    'PriceLvl_3',
    'PriceLvl_4',
    'PriceLvl_5',
    'PriceLvl_6',
    'PriceLvl_7',
    'PriceLvl_8',
    'PriceLvl_9',
    'PriceLvl_10',
    'PriceLvl_15',
    'PriceLvl_20',
    'PriceLvl_30',
    'PriceLvl_40',
    'PriceLvl_1_airbnb',
    'PriceLvl_2_airbnb',
    'PriceLvl_3_airbnb',
    'PriceLvl_4_airbnb',
    'PriceLvl_5_airbnb',
    'PriceLvl_6_airbnb',
    'PriceLvl_7_airbnb',
    'PriceLvl_8_airbnb',
    'PriceLvl_9_airbnb',
    'PriceLvl_10_airbnb',
    'PriceLvl_15_airbnb',
    'Beds_1_airbnb',
    'Beds_2_airbnb',
    'Beds_3_airbnb',
    'Beds_4_airbnb',
    'Beds_5_airbnb',
    'Beds_6_airbnb',
    'Beds_7_airbnb',
    'Beds_8_airbnb',
    'Beds_9_airbnb',
    'Beds_10_airbnb',
    'People_1_airbnb',
    'People_2_airbnb',
    'People_3_airbnb',
    'People_4_airbnb',
    'People_5_airbnb',
    'People_6_airbnb',
    'People_7_airbnb',
    'People_8_airbnb',
    'People_9_airbnb',
    'People_10_airbnb',
    'People_15_airbnb',
    'Reviews_1_airbnb',
    'Reviews_2_airbnb',
    'Reviews_3_airbnb',
    'Reviews_4_airbnb',
    'Reviews_5_airbnb',
    'Beach',
    'Nature',
    'Cultural',
    'Historical',
    'Adventurous',
    'EarlyMorning',
    'Morning',
    'Noon',
    'Afternoon',
    'Evening',
    'Night',
    'Label',
    'Click',
    'A Coruña',
    'Agadir',
    'Alicante',
    'Almería',
    'Asturias',
    'Badajoz',
    'Barcelona',
    'Bilbao',
    'Brindisi',
    'Béziers',
    'Donostia / San Sebastián',
    'Fuerteventura',
    'Girona',
    'Granada',
    'Ibiza',
    'Jerez de la Frontera',
    'Lanzarote',
    'Madrid',
    'Melilla',
    'Menorca',
    'Málaga',
    'Palma, Majorca',
    'Pamplona',
    'Santander',
    'Santiago de Compostela',
    'Seville',
    'Tenerife',
    'Valencia',
    'Valladolid',
    'Valverde',
    'Vigo',
    'Vitoria-Gasteiz',
    'Zaragoza']
    assert list(data_strcture()[2].columns) == test_pool_col
    assert len(data_strcture()[2]) == 1
    assert len(data_strcture()[2].columns) == 101
    
def test_Flights_data():
    test_col = ['flyFrom',
    'flyTo',
    'price',
    'cityFrom',
    'cityTo',
    'countryFrom',
    'distance',
    'duration',
    'local_departure',
    'category']
    assert list(flights_dataset().columns) == test_col

def test_Places_data():
    assert 1 == 1

def test_Ranges():
    assert len(Ranges()) == 7

    price_ranges_values = {'PriceLvl_1': [0, 100], 'PriceLvl_2': [100, 200], 'PriceLvl_3': [200, 300], 'PriceLvl_4': [300, 400], 
                    'PriceLvl_5': [400, 500], 'PriceLvl_6': [500, 600], 'PriceLvl_7': [600, 700], 'PriceLvl_8': [700, 800], 
                    'PriceLvl_9': [800, 900], 'PriceLvl_10': [900, 1000], 'PriceLvl_15': [1000, 1500], 
                    'PriceLvl_20': [1500, 2000], 'PriceLvl_30': [2000, 3000], 'PriceLvl_40': [3000, 4000]}
    time_ranges_values = {
        'EarlyMorning': [4, 7],
        'Morning': [7, 12],
        'Noon': [12, 16],
        'Afternoon': [16, 19],
        'Evening': [19, 23],
        'Night': [0, 4]
    }
    cities_dict_values = {'Tirana': 'TIA',
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

    assert Ranges()[0] == price_ranges_values
    assert Ranges()[1] == time_ranges_values
    assert Ranges()[2] == cities_dict_values
 
def test_user_data():
    df = pd.read_csv('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/Flights.csv')
    user_df = data_strcture()[1]
    pool_df = data_strcture()[0]
    city = 'Madrid'
    cat = 'Historical'
    price = 200
    price_airbnb = 55
    beds_airbnb = 2
    people_airbnb = 2
    reviews_airbnb = 100
    time = '2023-04-15 14:30:45'
    indicator = 0
    records, data_temp = users(0, df, user_df, pool_df, city, cat, price, price_airbnb, beds_airbnb, people_airbnb, reviews_airbnb, time, indicator)
    
    test_records_col = ['flyFrom', 'flyTo', 'price', 'cityFrom', 'cityTo', 'countryFrom',
       'distance', 'duration', 'local_departure', 'category', 'inptTime',
       'inptCat', 'inptPrice', 'inptCity', 'Label']
    assert list(records.columns) == test_records_col
    
    test_data_temp_col = ['PriceLvl_1', 'PriceLvl_2', 'PriceLvl_3', 'PriceLvl_4', 'PriceLvl_5',
       'PriceLvl_6', 'PriceLvl_7', 'PriceLvl_8', 'PriceLvl_9', 'PriceLvl_10',
       'PriceLvl_15', 'PriceLvl_20', 'PriceLvl_30', 'PriceLvl_40',
       'PriceLvl_1_airbnb', 'PriceLvl_2_airbnb', 'PriceLvl_3_airbnb',
       'PriceLvl_4_airbnb', 'PriceLvl_5_airbnb', 'PriceLvl_6_airbnb',
       'PriceLvl_7_airbnb', 'PriceLvl_8_airbnb', 'PriceLvl_9_airbnb',
       'PriceLvl_10_airbnb', 'PriceLvl_15_airbnb', 'Beds_1_airbnb',
       'Beds_2_airbnb', 'Beds_3_airbnb', 'Beds_4_airbnb', 'Beds_5_airbnb',
       'Beds_6_airbnb', 'Beds_7_airbnb', 'Beds_8_airbnb', 'Beds_9_airbnb',
       'Beds_10_airbnb', 'People_1_airbnb', 'People_2_airbnb',
       'People_3_airbnb', 'People_4_airbnb', 'People_5_airbnb',
       'People_6_airbnb', 'People_7_airbnb', 'People_8_airbnb',
       'People_9_airbnb', 'People_10_airbnb', 'People_15_airbnb',
       'Reviews_1_airbnb', 'Reviews_2_airbnb', 'Reviews_3_airbnb',
       'Reviews_4_airbnb', 'Reviews_5_airbnb', 'Beach', 'Nature', 'Cultural',
       'Historical', 'Adventurous', 'UserId', 'EarlyMorning', 'Morning',
       'Noon', 'Afternoon', 'Evening', 'Night', 'A Coruña', 'Agadir',
       'Alicante', 'Almería', 'Asturias', 'Badajoz', 'Barcelona', 'Bilbao',
       'Brindisi', 'Béziers', 'Donostia / San Sebastián', 'Fuerteventura',
       'Girona', 'Granada', 'Ibiza', 'Jerez de la Frontera', 'Lanzarote',
       'Madrid', 'Melilla', 'Menorca', 'Málaga', 'Palma, Majorca', 'Pamplona',
       'Santander', 'Santiago de Compostela', 'Seville', 'Tenerife',
       'Valencia', 'Valladolid', 'Valverde', 'Vigo', 'Vitoria-Gasteiz',
       'Zaragoza']
    assert list(data_temp.columns) == test_data_temp_col 
    
        
## models –-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------–-
    
def test_flights_reco():
    df = pd.read_csv('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/df.csv').reset_index()
    titles = pd.Series(df['Description'])
    indices = pd.Series(df.index, index = df['Description'])
    cosine_sim = np.load('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/cosine_sim.npy')
    
    reco = flights_reco('TIA','ALC','ALC',titles,indices,cosine_sim,df)
    reco_col = ['index', 'flyFrom', 'flyTo', 'price', 'cityFrom', 'cityTo',
       'countryFrom', 'distance', 'duration', 'local_departure', 'category',
       'Description']
    assert list(reco.columns) == reco_col
    
def test_model_clf():
    cosine_sim = np.load('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/cosine_sim.npy')
    
    reco, City, Category, Price_flight, time = clf(data_strcture()[1],data_strcture()[0],cosine_sim, 'INI')
    
    test_reco_keys = ['flyFrom', 'flyTo', 'price', 'cityFrom', 'cityTo', 'countryFrom',
       'distance', 'duration', 'local_departure', 'category', 'Description']
    assert list(reco.keys()) == test_reco_keys
    
    assert type(City) == str
    assert type(Category) == str
    assert type(Price_flight) == np.int64
    assert type(time) == str
    
def test_model_air():
    cosine_sim = np.load('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/cosine_sim_air.npy')
    df = pd.read_csv('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/Flights.csv')
    user_df = data_strcture()[1]
    pool_df = data_strcture()[0]
    pool_df, user_df, reco, City, Category, Price_flight, time, Price_Air,Beds_air,People_air,Reviews_air = clf_Airbnb(0, user_df, pool_df, df, 'Madrid', 200, 'Historical', '2023-04-15 14:30:45')
    
    test_pool_col = ['flyFrom', 'flyTo', 'price', 'cityFrom', 'cityTo', 'countryFrom',
       'distance', 'duration', 'local_departure', 'category']
    assert list(pool_df.columns) == test_pool_col
    
    test_user_col = ['PriceLvl_1', 'PriceLvl_2', 'PriceLvl_3', 'PriceLvl_4', 'PriceLvl_5',
       'PriceLvl_6', 'PriceLvl_7', 'PriceLvl_8', 'PriceLvl_9', 'PriceLvl_10',
       'PriceLvl_15', 'PriceLvl_20', 'PriceLvl_30', 'PriceLvl_40',
       'PriceLvl_1_airbnb', 'PriceLvl_2_airbnb', 'PriceLvl_3_airbnb',
       'PriceLvl_4_airbnb', 'PriceLvl_5_airbnb', 'PriceLvl_6_airbnb',
       'PriceLvl_7_airbnb', 'PriceLvl_8_airbnb', 'PriceLvl_9_airbnb',
       'PriceLvl_10_airbnb', 'PriceLvl_15_airbnb', 'Beds_1_airbnb',
       'Beds_2_airbnb', 'Beds_3_airbnb', 'Beds_4_airbnb', 'Beds_5_airbnb',
       'Beds_6_airbnb', 'Beds_7_airbnb', 'Beds_8_airbnb', 'Beds_9_airbnb',
       'Beds_10_airbnb', 'People_1_airbnb', 'People_2_airbnb',
       'People_3_airbnb', 'People_4_airbnb', 'People_5_airbnb',
       'People_6_airbnb', 'People_7_airbnb', 'People_8_airbnb',
       'People_9_airbnb', 'People_10_airbnb', 'People_15_airbnb',
       'Reviews_1_airbnb', 'Reviews_2_airbnb', 'Reviews_3_airbnb',
       'Reviews_4_airbnb', 'Reviews_5_airbnb', 'Beach', 'Nature', 'Cultural',
       'Historical', 'Adventurous', 'UserId', 'EarlyMorning', 'Morning',
       'Noon', 'Afternoon', 'Evening', 'Night', 'A Coruña', 'Agadir',
       'Alicante', 'Almería', 'Asturias', 'Badajoz', 'Barcelona', 'Bilbao',
       'Brindisi', 'Béziers', 'Donostia / San Sebastián', 'Fuerteventura',
       'Girona', 'Granada', 'Ibiza', 'Jerez de la Frontera', 'Lanzarote',
       'Madrid', 'Melilla', 'Menorca', 'Málaga', 'Palma, Majorca', 'Pamplona',
       'Santander', 'Santiago de Compostela', 'Seville', 'Tenerife',
       'Valencia', 'Valladolid', 'Valverde', 'Vigo', 'Vitoria-Gasteiz',
       'Zaragoza']
    assert list(user_df.columns) == test_user_col
    
    test_reco_keys = ['id', 'listing_url', 'description', 'host_is_superhost',
       'neighbourhood_cleansed', 'latitude', 'longitude', 'property_type',
       'room_type', 'accommodates', 'bathrooms_text', 'beds', 'amenities',
       'price', 'minimum_nights', 'maximum_nights', 'minimum_minimum_nights',
       'maximum_minimum_nights', 'has_availability', 'number_of_reviews',
       'instant_bookable', 'City', 'comments', 'Text', 'People',
       'Min_Duration', 'fear', 'anger', 'anticip', 'trust', 'surprise',
       'positive', 'negative', 'sadness', 'disgust', 'joy'] 
    assert list(reco.keys()) == test_reco_keys
    
    assert type(City) == str
    assert type(Category) == str
    assert type(Price_flight) == int
    assert type(time) == str
    assert type(Price_Air) == np.float64
    assert type(Beds_air) == np.float64
    assert type(People_air) == np.float64
    assert type(Reviews_air) == np.int64
    
def test_Places_reco():
    assert 1 == 1
    
