from Flights import flights_dataset
df = flights_dataset()
import datetime
#userid = 0
import pandas as pd
def users(userid ,df, user_df, pool_df, city, cat, price, time, indicator):
    #global userid 
    #print(df, user_df, pool_df, city, cat, price, time, indicator)
    #user_data = user_df
    #print('/////////////////////',indicator)

    def like_price_city_cat_time(userid, city, cat, price, time, user_df):
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        user_df.loc[user_df['UserId'] == userid, city] += 1
        user_df.loc[user_df['UserId'] == userid, cat] += 1
        if 4 <= time.hour < 7:
            user_df.loc[user_df['UserId'] == userid, 'EarlyMorning'] += 1
        elif 7 <= time.hour < 12:
            user_df.loc[user_df['UserId'] == userid, 'Morning'] += 1
        elif 12 <= time.hour < 16:
            user_df.loc[user_df['UserId'] == userid, 'Noon'] += 1
        elif 16 <= time.hour < 19:
            user_df.loc[user_df['UserId'] == userid, 'Afternoon'] += 1
        elif 19 <= time.hour < 23:
            user_df.loc[user_df['UserId'] == userid, 'Evening'] += 1
        else:
            user_df.loc[user_df['UserId'] == userid, 'Night'] += 1

        price_levels = {100: 'PriceLvl_1', 200: 'PriceLvl_2', 300: 'PriceLvl_3', 400: 'PriceLvl_4', 500: 'PriceLvl_5',
                        600: 'PriceLvl_6', 700: 'PriceLvl_7', 800: 'PriceLvl_8', 900: 'PriceLvl_9', 1000: 'PriceLvl_10',
                        1500: 'PriceLvl_15', 2000: 'PriceLvl_20', 3000: 'PriceLvl_30', 4000: 'PriceLvl_40'}

        for i in range(1, 21):
            if price < i * 100:
                user_df.loc[user_df['UserId']==userid, f'PriceLvl_{i}'] += 1
                break

        return user_df



    def dislike_price_city_cat_time(userid, city, cat, price, time, user_df):
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        user_df.loc[(user_df['UserId']==userid), city] -= 1
        user_df.loc[(user_df['UserId']==userid), cat] -= 1
        if time.hour >= 4 and time.hour < 7:
            user_df.loc[(user_df['UserId']==userid), 'EarlyMorning'] -=1
        if time.hour >= 7 and time.hour < 12:
            user_df.loc[(user_df['UserId']==userid), 'Morning'] -=1
        if time.hour >= 12 and time.hour < 16:
            user_df.loc[(user_df['UserId']==userid), 'Noon'] -=1
        if time.hour >= 16 and time.hour < 19:
            user_df.loc[(user_df['UserId']==userid), 'Afternoon'] -=1
        if time.hour >= 19 and time.hour < 23:
            user_df.loc[(user_df['UserId']==userid), 'Evening'] -=1
        if time.hour >= 24 and time.hour < 4:
            user_df.loc[(user_df['UserId']==userid), 'Night'] -=1
        if price < 100:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_1'] -= 1
        elif price < 200 and price >= 100:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_2'] -= 1
        elif price < 300 and price >= 200:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_3'] -= 1
        elif price < 400 and price >= 300:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_4'] -= 1
        elif price < 500 and price >= 400:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_5'] -= 1
        elif price < 600 and price >= 500:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_6'] -= 1
        elif price < 700 and price >= 600:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_7'] -= 1
        elif price < 800 and price >= 700:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_8'] -= 1
        elif price < 900 and price >= 800:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_9'] -= 1
        elif price < 1000 and price >= 900:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_10'] -= 1
        elif price < 1500 and price >= 1000:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_15'] -= 1
        elif price < 2000 and price >= 1500:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_20'] -= 1
        elif price < 3000 and price >= 2000:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_30'] -= 1
        elif price < 4000 and price >= 3000:
            user_df.loc[(user_df['UserId']==userid),'PriceLvl_40'] -= 1
        return user_df


    shared_cols = list(set(user_df.columns) & set(pool_df.columns))

    def record_interaction(userid, city, cat, price, time, indicator,pool_df):
        #global pool_df
        
        new_row = pd.DataFrame({col: [0] for col in pool_df.columns})
        new_row[shared_cols] = user_df.loc[(user_df['UserId']==userid)][shared_cols].values
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        new_row['inptTime'] = time
        new_row['inptCat'] = cat
        new_row['inptPrice'] = price
        new_row['inptCity'] = city
        if indicator == 0:
            new_row['Label'] = 0
        else:
            new_row['Label'] = 1
        pool_df = pool_df.append(new_row, ignore_index=True)
        return pool_df
    records = record_interaction(userid, city, cat, price, time, indicator,pool_df)
    data_temp = None
    if indicator == 0:
        data_temp = dislike_price_city_cat_time(userid, city, cat, price, time, user_df)
    elif indicator == 1:
        data_temp = like_price_city_cat_time(userid, city, cat, price, time, user_df)
    #print(user_data)
    return records, data_temp