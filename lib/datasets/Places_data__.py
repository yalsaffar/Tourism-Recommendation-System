import pandas as pd
def Places_data():
    places_in_spain = pd.read_csv("../datasets/data_files/places_activities_spain.csv")
    return places_in_spain