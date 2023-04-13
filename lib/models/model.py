import sys

# Add a path to sys.path
sys.path.append('../datasets')
from flights import  flights_reco
from userdata import users
from data_structure import data_strcture
from Ranges import Ranges
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")




#titles,indices, cosine_sim, df = model_computations()
def clf(counter , cosine_sim,user_df, pool_df,previous='ALC'):
    #titles,indices, cosine_sim, df = model_computations()
    titles = pd.read_csv('../datasets/data_files/titles.csv')
    df = pd.read_csv('../datasets/data_files/df.csv')
    df2 = df.reset_index()
    titles = pd.Series(df2['Description'])
    indices = pd.Series(df2.index, index = df2['Description'])
    cosine_sim = np.load('../datasets/data_files/cosine_sim.npy')
    
    #_, user_df, pool_df = data_strcture()


    def Flights_Reco(location, previous,best):
        
        recos = flights_reco(location,previous,best,titles,indices, cosine_sim,df)
        return recos.head(50)

    price_ranges, time_cols_dict, cities_dict = Ranges()
    

    
    
    location = input()

    city_names = list(set(df['cityTo'])) # Replace with your desired cities
    city_counts = user_df.filter(items=city_names).sum().sort_values(ascending=False)

    highest_city = city_counts.index[0]
    second_highest_city = city_counts.index[1]
    third_highest_city = city_counts.index[2]

    price_max_col = user_df.filter(like='PriceLvl_').idxmax(axis=1)
    activity_max_col = user_df.filter(['Beach', 'Nature', 'Cultural', 'Historical', 'Adventurous']).idxmax(axis=1)
    time_max_col = user_df.filter(['EarlyMorning', 'Morning', 'Noon', 'Afternoon', 'Evening', 'Night']).idxmax(axis=1)
    
    if counter != 3:
        reco = Flights_Reco(location,previous,cities_dict[highest_city])
    elif counter == 6:
        reco = Flights_Reco(location,previous,cities_dict[third_highest_city])
    else:
        reco = Flights_Reco(location,previous,cities_dict[second_highest_city])
    reco['local_departure'] = pd.to_datetime(reco['local_departure'])

    reco_filtered = reco[(reco['price'] >= price_ranges[str(price_max_col[0])][0]) & (reco['price'] <= price_ranges[str(price_max_col[0])][1])]
    reco_filtered2 = reco_filtered[(reco_filtered['local_departure'].dt.hour >= time_cols_dict[str(time_max_col[0])][0]) & (reco_filtered['local_departure'].dt.hour <= time_cols_dict[str(time_max_col[0])][1])]
    reco_filtered3 = reco_filtered2[reco_filtered2['category']== str(activity_max_col[0])]

    reco_others = reco[(reco['price'] < price_ranges[str(price_max_col[0])][0]) | (reco['price'] > price_ranges[str(price_max_col[0])][1])]
    reco_others2 = reco_filtered[(reco_filtered['local_departure'].dt.hour < time_cols_dict[str(time_max_col[0])][0]) | (reco_filtered['local_departure'].dt.hour > time_cols_dict[str(time_max_col[0])][1])]
    reco_others3 = reco_filtered2[reco_filtered2['category']!= str(activity_max_col[0])]

    reco_final = pd.concat([reco_filtered,reco_filtered2,reco_filtered3, reco_others,reco_others2,reco_others3])
    reco_final = reco_final.drop_duplicates(keep='first')

    previous = reco_final['flyTo'].iloc[0]

    print(reco_final.head(1))
    print("Do you like this offer: (yes:1, no:0)")
    indicator = input()
    
    
    pool_df, user_df = users(0 ,df, user_df, pool_df, reco_final['cityTo'].iloc[0], reco_final['category'].iloc[0], reco_final['price'].iloc[0], str(reco_final['local_departure'].iloc[0]), indicator)
    return pool_df, user_df 
