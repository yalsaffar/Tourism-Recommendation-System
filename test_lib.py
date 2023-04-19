import sys
import os
import io
import pandas as pd
import numpy as np
import pytest
import warnings
    
warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir('/Users/SaadDev/Tourism-Recommendation-System/lib')


sys.path.append('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets')

from Flights import flights_dataset
from Airbnb_data import Airbnb_data
from data_structure import data_strcture
from Ranges import Ranges
from userdata import users

sys.path.append('/Users/SaadDev/Tourism-Recommendation-System/lib/models')

from Airbnb_reco import Airbnb_reco
from flights import flights_reco
from model import clf
from Places_reco import Places_reco

# Library

## datasets –-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------

def test_Airbnb_data():
    df = Airbnb_data()
    test_col = ['index', 'id', 'listing_url', 'name', 'description',
       'host_is_superhost', 'neighbourhood_cleansed', 'latitude', 'longitude',
       'property_type', 'room_type', 'accommodates', 'bathrooms_text', 'beds',
       'amenities', 'price', 'minimum_nights', 'maximum_nights',
       'minimum_minimum_nights', 'maximum_minimum_nights',
       'minimum_maximum_nights', 'maximum_maximum_nights',
       'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm', 'has_availability',
       'availability_30', 'availability_60', 'availability_90',
       'availability_365', 'calendar_last_scraped', 'number_of_reviews',
       'number_of_reviews_ltm', 'number_of_reviews_l30d', 'instant_bookable',
       'calculated_host_listings_count',
       'calculated_host_listings_count_entire_homes',
       'calculated_host_listings_count_private_rooms',
       'calculated_host_listings_count_shared_rooms', 'comments']
    assert list(df.columns) == test_col

def test_data_structure():
    assert len(data_strcture()) == 3
    df = data_strcture()[0]
    user_df = data_strcture()[1]
    pool_df = data_strcture()[2]

    test_df_col = ['flyFrom',
    'flyTo',
    'price',
    'cityFrom',
    'cityTo',
    'countryFrom',
    'distance',
    'duration',
    'local_departure',
    'category']
    assert list(df.columns) == test_df_col

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
    assert list(user_df.columns) == test_user_col
    assert len(user_df.columns) == 59
        
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
    assert list(pool_df.columns) == test_pool_col
    assert len(pool_df) == 1
    assert len(pool_df.columns) == 64
    
def test_Flights():
    df = flights_dataset()
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
    assert list(df.columns) == test_col

def test_Places_data():
    assert 1 == 1

def test_Ranges():
    assert len(Ranges()) == 3
    
    price_ranges = Ranges()[0]
    time_ranges = Ranges()[1]
    cities_dict = Ranges()[2]

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

    assert price_ranges == price_ranges_values
    assert time_ranges == time_ranges_values
    assert cities_dict == cities_dict_values
 
def test_user_data():
    assert 1 == 1
    
## models –-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------–-----------–-

def test_Airbnb_reco():
    assert 1 == 1
    
def test_flights():
    location = 'TIA'
    previous = 'ALC'
    best = 'ALC'

    df = pd.read_csv('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/df.csv')
    df = df.reset_index()

    titles = pd.Series(df['Description'])
    indices = pd.Series(df.index, index = df['Description'])
    user_df = data_strcture()[1]
    cosine_sim = np.load('/Users/SaadDev/Tourism-Recommendation-System/lib/datasets/data_files/cosine_sim.npy')
    
    reco = flights_reco('TIA','ALC','ALC',titles,indices,cosine_sim,df)
    reco_col = ['index', 'flyFrom', 'flyTo', 'price', 'cityFrom', 'cityTo',
       'countryFrom', 'distance', 'duration', 'local_departure', 'category',
       'Description']
    assert list(reco.columns) == reco_col
    
def test_model(monkeypatch):
    c = np.load('../datasets/data_files/cosine_sim.npy')
    
    pool_df, user_df = clf(data_strcture()[1],data_strcture()[2],c)
    assert pool_df is not None
    assert user_df is not None
    
    pool_df_col = ['inptCity', 'inptTime', 'inptCat', 'inptPrice', 'PriceLvl_1',
       'PriceLvl_2', 'PriceLvl_3', 'PriceLvl_4', 'PriceLvl_5', 'PriceLvl_6',
       'PriceLvl_7', 'PriceLvl_8', 'PriceLvl_9', 'PriceLvl_10', 'PriceLvl_15',
       'PriceLvl_20', 'PriceLvl_30', 'PriceLvl_40', 'Beach', 'Nature',
       'Cultural', 'Historical', 'Adventurous', 'EarlyMorning', 'Morning',
       'Noon', 'Afternoon', 'Evening', 'Night', 'Label', 'Click', 'A Coruña',
       'Agadir', 'Alicante', 'Almería', 'Asturias', 'Badajoz', 'Barcelona',
       'Bilbao', 'Brindisi', 'Béziers', 'Donostia / San Sebastián',
       'Fuerteventura', 'Girona', 'Granada', 'Ibiza', 'Jerez de la Frontera',
       'Lanzarote', 'Madrid', 'Melilla', 'Menorca', 'Málaga', 'Palma, Majorca',
       'Pamplona', 'Santander', 'Santiago de Compostela', 'Seville',
       'Tenerife', 'Valencia', 'Valladolid', 'Valverde', 'Vigo',
       'Vitoria-Gasteiz', 'Zaragoza']
    assert list(pool_df.columns) == pool_df_col
    
    user_df_col = ['PriceLvl_1',
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
    assert list(user_df.columns) == user_df_col
    
def test_Places_reco():
    assert 1 == 1
    
