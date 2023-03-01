import pandas as pd
import ast


def flights_dataset():
    flights = pd.read_csv('flights_data_002.csv')
    flights['MeanPrice'] = flights.groupby(['flyTo','cityFrom'])['price'].transform('mean') 
    flights['DiffMeanPrice'] = flights.groupby(['flyTo','cityFrom'])['price'].transform('mean') - flights['price']
    flights['flight_route'] = flights['flyFrom'] + ' ' + flights['flyTo'] + ' ' + flights['cityFrom'] + ' ' + flights['cityTo']
    flights['soup'] = flights['flight_route'] + ' '+ flights['airlines'] 
    flights = flights.dropna()
    remove_duplicates = lambda x: {k: v for k, v in x.items() if len(x) == 1 or k == '1'}
    flights['bags_price'] = flights['bags_price'].apply(ast.literal_eval)
    flights['bags_price'] = flights['bags_price'].apply(remove_duplicates)
    flights['bags_price'] = flights['bags_price'].apply(lambda x: x['1'] if isinstance(x, dict) and '1' in x else x)

    return flights


