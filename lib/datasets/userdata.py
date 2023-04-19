from Flights import flights_dataset
df = flights_dataset()
import datetime
#userid = 0
import pandas as pd
def users(userid ,df, user_df, pool_df, city, cat, price,price_airbnb,beds_airbnb,people_airbnb,reviews_airbnb,place_category, place_time, time, indicator):
    """
    Update the user and pool data based on the user's interaction with a property.

    Args:
        userid (int): The ID of the user.
        df (pandas DataFrame): The data of the property the user interacted with.
        user_df (pandas DataFrame): The user data.
        pool_df (pandas DataFrame): The pool data.
        city (str): The city of the property.
        cat (str): The category of the property.
        price (int): The price of the property.
        price_airbnb (int): The price of similar properties on Airbnb.
        beds_airbnb (int): The number of beds in similar properties on Airbnb.
        people_airbnb (int): The maximum number of people that can stay in similar properties on Airbnb.
        reviews_airbnb (int): The average number of reviews of similar properties on Airbnb.
        place_category (str): The category of the place where the property is located.
        place_time (str): The time period when the property is available.
        time (str): The time when the user interacted with the property.
        indicator (int): Whether the user liked (1) or disliked (0) the property.

    Returns:
        records (pandas DataFrame): The updated pool data.
        data_temp (pandas DataFrame): The updated user data.
    """

    
    if city == 'Malaga':
        city = 'Málaga'
    #global userid 
    #print(df, user_df, pool_df, city, cat, price, time, indicator)
    #user_data = user_df
    #print('/////////////////////',indicator)

    def like(userid, city, cat, price,price_airbnb,beds_airbnb,people_airbnb,reviews_airbnb, place_category, place_time, time, user_df):
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

        user_df.loc[user_df['UserId'] == userid, place_category] += 1
        user_df.loc[user_df['UserId'] == userid, place_time] += 1

       
        for i in range(1, 21):
            if price < i * 100:
                user_df.loc[user_df['UserId']==userid, f'PriceLvl_{i}'] += 1
                break
        for i in range(1, 21):
            if price_airbnb < i * 100:
                user_df.loc[user_df['UserId'] == userid, f'PriceLvl_{i}_airbnb'] += 1
                break
        for i in range(1, 11):
            if beds_airbnb == i:
                user_df.loc[user_df['UserId'] == userid, f'Beds_{i}_airbnb'] += 1
                break
        for i in range(1, 11):
            if people_airbnb <= i:
                user_df.loc[user_df['UserId'] == userid, f'People_{i}_airbnb'] += 1
                break
        for i in range(1, 6):
            if reviews_airbnb <= i * 200:
                user_df.loc[user_df['UserId'] == userid, f'Reviews_{i}_airbnb'] += 1
                break

        return user_df



    def dislike(userid, city, cat, price,price_airbnb,beds_airbnb,people_airbnb,reviews_airbnb, place_category, place_time, time, user_df):
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        user_df.loc[user_df['UserId'] == userid, city] -= 1
        user_df.loc[user_df['UserId'] == userid, cat] -= 1
        if 4 <= time.hour < 7:
            user_df.loc[user_df['UserId'] == userid, 'EarlyMorning'] -= 1
        elif 7 <= time.hour < 12:
            user_df.loc[user_df['UserId'] == userid, 'Morning'] -= 1
        elif 12 <= time.hour < 16:
            user_df.loc[user_df['UserId'] == userid, 'Noon'] -= 1
        elif 16 <= time.hour < 19:
            user_df.loc[user_df['UserId'] == userid, 'Afternoon'] -= 1
        elif 19 <= time.hour < 23:
            user_df.loc[user_df['UserId'] == userid, 'Evening'] -= 1
        else:
            user_df.loc[user_df['UserId'] == userid, 'Night'] -= 1

        user_df.loc[userid, place_category] -= 1
        user_df.loc[userid, place_time] -= 1
            
        for i in range(1, 21):
            if price < i * 100:
                user_df.loc[user_df['UserId']==userid, f'PriceLvl_{i}'] -= 1
                break
                
        for i in range(1, 21):
            if price_airbnb < i * 100:
                user_df.loc[user_df['UserId'] == userid, f'PriceLvl_{i}_airbnb'] -= 1
                break
                
        for i in range(1, 11):
            if beds_airbnb == i:
                user_df.loc[user_df['UserId'] == userid, f'Beds_{i}_airbnb'] -= 1
                break
                
        for i in range(1, 11):
            if people_airbnb <= i:
                user_df.loc[user_df['UserId'] == userid, f'People_{i}_airbnb'] -= 1
                break
                
        for i in range(1, 6):
            if reviews_airbnb <= i * 200:
                user_df.loc[user_df['UserId'] == userid, f'Reviews_{i}_airbnb'] -= 1
                break
                
        return user_df



    shared_cols = list(set(user_df.columns) & set(pool_df.columns))

    def record_interaction(userid, city, cat, price,price_airbnb,beds_airbnb,people_airbnb,reviews_airbnb,place_category, place_time, time, indicator,pool_df):
        #global pool_df
        
        new_row = pd.DataFrame({col: [0] for col in pool_df.columns})
        new_row[shared_cols] = user_df.loc[(user_df['UserId']==userid)][shared_cols].values
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        new_row['inptTime'] = time
        new_row['inptCat'] = cat
        new_row['inptPrice'] = price
        new_row['inptCity'] = city
        new_row['inptPriceAir'] = price_airbnb
        new_row['inptBedsAir'] = beds_airbnb
        new_row['inptPeopleAir'] = people_airbnb
        new_row['inptReviewsAir'] = reviews_airbnb
        new_row['inptPlaceCat'] = place_category
        new_row['inptPlaceTime'] = place_time
        if indicator == 0:
            new_row['Label'] = 0
        else:
            new_row['Label'] = 1
        pool_df = pool_df.append(new_row, ignore_index=True)
        return pool_df
    records = record_interaction(userid, city, cat, price,price_airbnb,beds_airbnb,people_airbnb,reviews_airbnb,place_category, place_time, time, indicator,pool_df)
    data_temp = None
    if indicator == 0:
        data_temp = dislike(userid, city, cat, price,price_airbnb,beds_airbnb,people_airbnb,reviews_airbnb,place_category, place_time, time, user_df)
    elif indicator == 1:
        data_temp = like(userid, city, cat, price,price_airbnb,beds_airbnb,people_airbnb,reviews_airbnb,place_category, place_time, time, user_df)
    #print(user_data)
    return records, data_temp