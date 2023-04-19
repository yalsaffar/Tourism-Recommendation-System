import pandas as pd


def flights_dataset():
    """
    This function loads a flights dataset from a CSV file and performs some preprocessing on it.
    - Reads the CSV file from '../datasets/data_files/flights_data_002.csv'
    - Drops the 'conversion' column
    - Converts 'local_arrival' and 'local_departure' columns to datetime format
    - Fills missing values in 'bags_price' and 'availability' columns by grouping flights by 'distance' and
      filling them with the first non-null value within each group
    - Creates a dictionary with city-category score pairs
    - Extracts the city and assigns a category score to it based on the above dictionary
    - Drops unnecessary columns such as 'fare', 'luggage_weight', 'availability', 'local_arrival', 'airlines',
      'score', 'bags_price', and 'countryTo'
    - Returns the preprocessed DataFrame
    """

    df = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/flights_data_002.csv")
    df = df.drop(['conversion'], axis=1)
    df['local_arrival'] = pd.to_datetime(df['local_arrival'])
    df['local_departure'] = pd.to_datetime(df['local_departure'])
    grouped_bag = df.groupby('distance')
    grouped_avl = df.groupby('distance')

    df['bags_price'] = grouped_bag['bags_price'].apply(lambda x: x.fillna(x.dropna().iloc[0]) if x.isnull().values.any() else x)
    df['availability'] = grouped_avl['availability'].apply(lambda x: x.fillna(x.dropna().iloc[0]) if x.isnull().values.any() else x)
    city_category_scores = {
    ('Málaga', 'Beach'): 8,
    ('Alicante', 'Beach'): 7,
    ('Almería', 'Beach'): 6,
    ('Asturias', 'Nature'): 9,
    ('Bilbao', 'Cultural'): 8,
    ('Barcelona', 'Cultural'): 9,
    ('Badajoz', 'Nature'): 7,
    ('Béziers', 'Adventurous'): 6,
    ('Brindisi', 'Adventurous'): 7,
    ('Donostia / San Sebastián', 'Nature'): 8,
    ('Fuerteventura', 'Beach'): 7,
    ('Girona', 'Cultural'): 8,
    ('Granada', 'Historical'): 9,
    ('Ibiza', 'Beach'): 7,
    ('Jerez de la Frontera', 'Cultural'): 7,
    ('A Coruña', 'Nature'): 8,
    ('Lanzarote', 'Beach'): 6,
    ('Madrid', 'Historical'): 9,
    ('Agadir', 'Beach'): 6,
    ('Menorca', 'Beach'): 7,
    ('Melilla', 'Historical'): 8,
    ('Palma, Majorca', 'Beach'): 8,
    ('Pamplona', 'Historical'): 7,
    ('Santander', 'Nature'): 8,
    ('Seville', 'Historical'): 9,
    ('Tenerife', 'Beach'): 7,
    ('Valencia', 'Cultural'): 8,
    ('Valladolid', 'Cultural'): 7,
    ('Vigo', 'Nature'): 7,
    ('Vitoria-Gasteiz', 'Nature'): 7,
    ('Valverde', 'Nature'): 6,
    ('Zaragoza', 'Cultural'): 8,
    ('Santiago de Compostela', 'Historical'): 8}
    cities = [key[0] for key in city_category_scores.keys()]
    categories = [key[1] for key in city_category_scores.keys()]
    scores = list(city_category_scores.values())

    df['category'] = df['cityTo'].apply(lambda x: categories[cities.index(x)] if x in cities else None)
    df['score'] = df['cityTo'].apply(lambda x: scores[cities.index(x)] if x in cities else None)
    df = df.drop(['fare', 'luggage_weight','availability','local_arrival','airlines','score','bags_price','countryTo'],axis=1)

    return df


