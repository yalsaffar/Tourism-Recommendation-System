import pandas as pd
import numpy as np
from Flights import flights_dataset
def data_strcture():
    """
    Returns three dataframes: 
    - `df`: a dataframe containing flight information 
    - `user_df`: a dataframe containing user information and preferences 
    - `pool_df`: a dataframe used to store recommended flights for each user 

    The `df` dataframe is generated from the `flights_dataset()` function. The `user_df` 
    dataframe has 1000 rows and contains columns for price levels, Airbnb price levels, 
    number of beds, number of people, Airbnb reviews, and user preferences for various 
    types of activities and times of day. The `pool_df` dataframe has one row and contains 
    columns for flight information, price levels, Airbnb price levels, number of beds, 
    number of people, Airbnb reviews, and user preferences for various types of activities 
    and times of day.
    """

    df = flights_dataset()
    pool_df = pd.DataFrame(index=range(1))
    pool_df['inptCity'] = np.nan
    pool_df['inptTime'] = np.nan
    pool_df['inptCat'] = np.nan
    pool_df['inptPrice'] = np.nan
    pool_df['PriceLvl_1'] = np.nan
    pool_df['PriceLvl_2'] = np.nan
    pool_df['PriceLvl_3'] = np.nan
    pool_df['PriceLvl_4'] = np.nan
    pool_df['PriceLvl_5'] = np.nan
    pool_df['PriceLvl_6'] = np.nan
    pool_df['PriceLvl_7'] = np.nan
    pool_df['PriceLvl_8'] = np.nan
    pool_df['PriceLvl_9'] = np.nan
    pool_df['PriceLvl_10'] = np.nan
    pool_df['PriceLvl_15'] = np.nan
    pool_df['PriceLvl_20'] = np.nan
    pool_df['PriceLvl_30'] = np.nan
    pool_df['PriceLvl_40'] = np.nan
    #---------------
    pool_df['PriceLvl_1_airbnb'] = np.nan
    pool_df['PriceLvl_2_airbnb'] = np.nan
    pool_df['PriceLvl_3_airbnb'] = np.nan
    pool_df['PriceLvl_4_airbnb'] = np.nan
    pool_df['PriceLvl_5_airbnb'] = np.nan
    pool_df['PriceLvl_6_airbnb'] = np.nan
    pool_df['PriceLvl_7_airbnb'] = np.nan
    pool_df['PriceLvl_8_airbnb'] = np.nan
    pool_df['PriceLvl_9_airbnb'] = np.nan
    pool_df['PriceLvl_10_airbnb'] = np.nan
    pool_df['PriceLvl_15_airbnb'] = np.nan
    #--------------
    #---------------
    pool_df['Beds_1_airbnb'] = np.nan
    pool_df['Beds_2_airbnb'] = np.nan
    pool_df['Beds_3_airbnb'] = np.nan
    pool_df['Beds_4_airbnb'] = np.nan
    pool_df['Beds_5_airbnb'] = np.nan
    pool_df['Beds_6_airbnb'] = np.nan
    pool_df['Beds_7_airbnb'] = np.nan
    pool_df['Beds_8_airbnb'] = np.nan
    pool_df['Beds_9_airbnb'] = np.nan
    pool_df['Beds_10_airbnb'] = np.nan
    #--------------
    #---------------
    pool_df['People_1_airbnb'] = np.nan
    pool_df['People_2_airbnb'] = np.nan
    pool_df['People_3_airbnb'] = np.nan
    pool_df['People_4_airbnb'] = np.nan
    pool_df['People_5_airbnb'] = np.nan
    pool_df['People_6_airbnb'] = np.nan
    pool_df['People_7_airbnb'] = np.nan
    pool_df['People_8_airbnb'] = np.nan
    pool_df['People_9_airbnb'] = np.nan
    pool_df['People_10_airbnb'] = np.nan
    pool_df['People_15_airbnb'] = np.nan
    #--------------
     #---------------
    pool_df['Reviews_1_airbnb'] = np.nan
    pool_df['Reviews_2_airbnb'] = np.nan
    pool_df['Reviews_3_airbnb'] = np.nan
    pool_df['Reviews_4_airbnb'] = np.nan
    pool_df['Reviews_5_airbnb'] = np.nan
    #--------------
    pool_df['Beach'] = np.nan
    pool_df['Nature'] = np.nan
    pool_df['Cultural'] = np.nan
    pool_df['Historical'] = np.nan
    pool_df['Adventurous'] = np.nan
    pool_df['EarlyMorning'] = np.nan
    pool_df['Morning'] = np.nan
    pool_df['Noon'] = np.nan
    pool_df['Afternoon'] = np.nan
    pool_df['Evening'] = np.nan
    pool_df['Night'] = np.nan
    pool_df['Label'] = np.nan
    pool_df['Click'] = np.nan
    dummy_df = pd.get_dummies(df['cityTo'])
    x = dummy_df.columns
    for y in x:
        pool_df[x] = y
    pool_df = pd.DataFrame(0, index=pool_df.index, columns=pool_df.columns)

    user_df = pd.DataFrame(index=range(1000))

    user_df['PriceLvl_1'] = np.nan
    user_df['PriceLvl_2'] = np.nan
    user_df['PriceLvl_3'] = np.nan
    user_df['PriceLvl_4'] = np.nan
    user_df['PriceLvl_5'] = np.nan
    user_df['PriceLvl_6'] = np.nan
    user_df['PriceLvl_7'] = np.nan
    user_df['PriceLvl_8'] = np.nan
    user_df['PriceLvl_9'] = np.nan
    user_df['PriceLvl_10'] = np.nan
    user_df['PriceLvl_15'] = np.nan
    user_df['PriceLvl_20'] = np.nan
    user_df['PriceLvl_30'] = np.nan
    user_df['PriceLvl_40'] = np.nan

    #---------------
    user_df['PriceLvl_1_airbnb'] = np.nan
    user_df['PriceLvl_2_airbnb'] = np.nan
    user_df['PriceLvl_3_airbnb'] = np.nan
    user_df['PriceLvl_4_airbnb'] = np.nan
    user_df['PriceLvl_5_airbnb'] = np.nan
    user_df['PriceLvl_6_airbnb'] = np.nan
    user_df['PriceLvl_7_airbnb'] = np.nan
    user_df['PriceLvl_8_airbnb'] = np.nan
    user_df['PriceLvl_9_airbnb'] = np.nan
    user_df['PriceLvl_10_airbnb'] = np.nan
    user_df['PriceLvl_15_airbnb'] = np.nan
    #--------------
    #---------------
    user_df['Beds_1_airbnb'] = np.nan
    user_df['Beds_2_airbnb'] = np.nan
    user_df['Beds_3_airbnb'] = np.nan
    user_df['Beds_4_airbnb'] = np.nan
    user_df['Beds_5_airbnb'] = np.nan
    user_df['Beds_6_airbnb'] = np.nan
    user_df['Beds_7_airbnb'] = np.nan
    user_df['Beds_8_airbnb'] = np.nan
    user_df['Beds_9_airbnb'] = np.nan
    user_df['Beds_10_airbnb'] = np.nan
    #--------------
    #---------------
    user_df['People_1_airbnb'] = np.nan
    user_df['People_2_airbnb'] = np.nan
    user_df['People_3_airbnb'] = np.nan
    user_df['People_4_airbnb'] = np.nan
    user_df['People_5_airbnb'] = np.nan
    user_df['People_6_airbnb'] = np.nan
    user_df['People_7_airbnb'] = np.nan
    user_df['People_8_airbnb'] = np.nan
    user_df['People_9_airbnb'] = np.nan
    user_df['People_10_airbnb'] = np.nan
    user_df['People_15_airbnb'] = np.nan
    #--------------
    #---------------
    user_df['Reviews_1_airbnb'] = np.nan
    user_df['Reviews_2_airbnb'] = np.nan
    user_df['Reviews_3_airbnb'] = np.nan
    user_df['Reviews_4_airbnb'] = np.nan
    user_df['Reviews_5_airbnb'] = np.nan
    #----------------
    user_df['Beach'] = np.nan
    user_df['Nature'] = np.nan
    user_df['Cultural'] = np.nan
    user_df['Historical'] = np.nan
    user_df['Adventurous'] = np.nan
    user_df['UserId'] = np.nan
    user_df['EarlyMorning'] = np.nan
    user_df['Morning'] = np.nan
    user_df['Noon'] = np.nan
    user_df['Afternoon'] = np.nan
    user_df['Evening'] = np.nan
    user_df['Night'] = np.nan

    #----------------
    new_columns_places = ['place_morning', 'place_afternoon', 'place_night' ,'place_adventurous', 'place_cultural', 'place_nature', 'place_beach', 'place_historical']
    for column in new_columns_places:
        user_df[column] = 0
        pool_df[column] = 0

    dummy_df = pd.get_dummies(df['cityTo'])
    x = dummy_df.columns
    for y in x:
        user_df[x] = y
    user_df = pd.DataFrame(0, index=user_df.index, columns=user_df.columns)
    user_df['UserId'] = range(1000)
    return df, user_df, pool_df