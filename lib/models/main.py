from model import clf, clf_Airbnb, clf_places
import pandas as pd
import numpy as np
from data_structure import data_strcture

from userdata import users
def main(UserId,location):
    user_df = pd.read_csv('../datasets/data_files/user_df.csv')
    pool_df = pd.read_csv('../datasets/data_files/pool_df.csv')
    # _, user_df, pool_df = data_strcture()
    df_air = pd.read_csv('../datasets/data_files/airbnb_clean.csv')
    df_flight = pd.read_csv('../datasets/data_files/df.csv')
    cosine_sim = np.load('../datasets/data_files/cosine_sim.npy')
    Reco_1, City, Category, Price_flight, time = clf( UserId,user_df, pool_df,cosine_sim,location,previous='ALC')
    # More cities are here, need to be fixed
    pool_df, user_df, Reco_2, City, Category, Price_flight, time, Price_Air,Beds_air,People_air,Reviews_air = clf_Airbnb(UserId,user_df,pool_df,df_air,City,Price_flight,Category,time,prev = 50059918)
    
    Reco_3,Category_place,Time_place = clf_places(City,UserId,user_df,previous = 712)

    return Reco_1, Reco_2, Reco_3,UserId , City, Category, Price_flight,Price_Air,Beds_air,People_air,Reviews_air, Category_place,Time_place, time, pool_df, user_df

def record(UserId , City, Category, Price_flight,Price_Air,Beds_air,People_air,Reviews_air, Category_place,Time_place, time, user_df, pool_df, indicator):
    df_air = pd.read_csv('../datasets/data_files/airbnb_clean.csv')

    pool_df, updated_user_df = users(UserId ,df_air, user_df, pool_df, City, Category, Price_flight,Price_Air,Beds_air,People_air,Reviews_air,Category_place, Time_place, time, int(indicator))
    user_df = updated_user_df.copy()

    user_df.to_csv('../datasets/data_files/user_df.csv',index=False)
    pool_df.to_csv('../datasets/data_files/pool_df.csv',index=False)