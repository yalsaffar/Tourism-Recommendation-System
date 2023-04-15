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

import warnings
warnings.filterwarnings("ignore")




#titles,indices, cosine_sim, df = model_computations()
def clf( user_df, pool_df,cosine_sim,location,previous='ALC'):
    #titles,indices, cosine_sim, df = model_computations()
    titles = pd.read_csv('../datasets/data_files/titles.csv')
    df = pd.read_csv('../datasets/data_files/df.csv')
    df2 = df.reset_index()
    titles = pd.Series(df2['Description'])
    indices = pd.Series(df2.index, index = df2['Description'])
    #cosine_sim = np.load('../datasets/data_files/cosine_sim.npy')
    
    #_, user_df, pool_df = data_strcture()


    def Flights_Reco(location, previous,best):
        
        recos = flights_reco(location,previous,best,titles,indices, cosine_sim,df)
        return recos.head(50)

    price_ranges, time_cols_dict, cities_dict = Ranges()
    

    
    #print(user_df)
    #location = input()

    city_names = list(set(df['cityTo'])) 
    city_counts = user_df.filter(items=city_names).sum().sort_values(ascending=False)

    highest_city = city_counts.index[0]
    #second_highest_city = city_counts.index[1]
    #third_highest_city = city_counts.index[2]

    price_max_col = user_df.filter(like='PriceLvl_').idxmax(axis=1)
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
    
    previous = reco_final['flyTo'].iloc[0]
    print("-------------------------------")
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
    titles = pd.read_csv('../datasets/data_files/titles_air.csv')
    df = pd.read_csv('../datasets/data_files/airbnb_clean.csv')
    df2 = df.reset_index()
    titles = pd.Series(df2['Text'])
    indices = pd.Series(df2.index, index = df2['Text'])
    cosine_sim = np.load('../datasets/data_files/cosine_sim_air.npy')
    recos = Airbnb_reco(location,previous,best_price,best_beds,best_People,best_reviews,titles,indices, cosine_sim, df)
    return recos.head(50)
        
def clf_Airbnb(UserId,user_df,pool_df,df,City,Price_flight,Category,time,prev = 50059918):
    price_ranges, time_cols_dict, cities_dict, price_ranges_air, beds_ranges, people_ranges, reviews_ranges = Ranges()
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
    print(City,prev, best_price_air,best_beds_air,best_people_air, best_reviews_air)

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
