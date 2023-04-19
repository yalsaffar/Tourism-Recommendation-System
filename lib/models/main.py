from model import clf, clf_Airbnb, clf_places
import pandas as pd
import numpy as np
from data_structure import data_strcture

from userdata import users
def main(UserId,location):

    """
    Returns recommendations for flights, Airbnb, and places to visit based on the user's preferences and previous activities.

    Args:
        UserId (int): The user ID.
        location (str): The user's preferred city for travel.

    Returns:
        tuple: A tuple containing:
            - DataFrame: Recommended flights
            - DataFrame: Recommended Airbnb listings
            - DataFrame: Recommended places to visit
            - int: The user ID
            - str: The recommended city
            - str: The recommended category
            - float: The recommended flight price
            - float: The recommended Airbnb price
            - int: The recommended number of beds in the Airbnb listing
            - int: The recommended number of people in the Airbnb listing
            - int: The recommended number of reviews for the Airbnb listing
            - str: The recommended category for places to visit
            - float: The recommended time to visit the recommended places
            - float: The total time taken for recommendations
            - DataFrame: The updated pool of flights and Airbnb listings
            - DataFrame: The updated user profile

    """

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
    """
    Records the user's selections and updates the user and pool dataframes.

    Args:
        UserId (int): The unique identifier of the user.
        City (str): The city recommended by the system.
        Category (str): The category recommended by the system.
        Price_flight (int): The price of the flight recommended by the system.
        Price_Air (int): The price of the Airbnb recommended by the system.
        Beds_air (int): The number of beds in the Airbnb recommended by the system.
        People_air (int): The number of people the Airbnb recommended by the system can accommodate.
        Reviews_air (int): The number of reviews for the Airbnb recommended by the system.
        Category_place (str): The category of the place recommended by the system.
        Time_place (str): The time recommended by the system.
        time (str): The time selected by the user.
        user_df (pd.DataFrame): The user dataframe.
        pool_df (pd.DataFrame): The pool dataframe.
        indicator (bool): The user's response indicating if the recommendations were satisfactory or not.

    Returns:
        None
    """

    df_air = pd.read_csv('../datasets/data_files/airbnb_clean.csv')

    pool_df, updated_user_df = users(UserId ,df_air, user_df, pool_df, City, Category, Price_flight,Price_Air,Beds_air,People_air,Reviews_air,Category_place, Time_place, time, int(indicator))
    user_df = updated_user_df.copy()

    user_df.to_csv('../datasets/data_files/user_df.csv',index=False)
    pool_df.to_csv('../datasets/data_files/pool_df.csv',index=False)