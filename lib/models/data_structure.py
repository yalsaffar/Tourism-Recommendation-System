import pandas as pd
import numpy as np
from Flights import flights_dataset
def data_strcture():
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

    user_df = pd.DataFrame(index=range(1))

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
    dummy_df = pd.get_dummies(df['cityTo'])
    x = dummy_df.columns
    for y in x:
        user_df[x] = y
    user_df = pd.DataFrame(0, index=user_df.index, columns=user_df.columns)
    user_df['UserId'] = range(1)
    return df, user_df, pool_df