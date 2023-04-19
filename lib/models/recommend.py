import pandas as pd
import gradio as gr
from main import main

def recommend(UserId, location):
    UserId = int(UserId)
    Reco_1, Reco_2, Reco_3, UserId, City, Category, Price_flight, Price_Air, Beds_air, People_air, Reviews_air, Category_place, Time_place, time, pool_df, user_df = main(UserId, location)
    
    # Create dictionary of results
    result = {
        "Recommendation 1": Reco_1,
        "Recommendation 2": Reco_2,
        "Recommendation 3": Reco_3,
        "UserId": UserId,
        "City": City,
        "Category": Category,
        "Price_flight": float(Price_flight),  # Convert numpy.int64 to float
        "Price_Air": float(Price_Air),  # Convert numpy.int64 to float
        "Beds_air": int(Beds_air),  # Convert numpy.int64 to int
        "People_air": int(People_air),  # Convert numpy.int64 to int
        "Reviews_air": float(Reviews_air),  # Convert numpy.float64 to float
        "Category_place": Category_place,
        "Time_place": Time_place,
        "time": time
    }
    
    # Convert dictionary to dataframe and then to JSON
    df = pd.DataFrame(pd.Series(result)).T
    json_str = df.to_json(orient="records")
    return json_str

iface = gr.Interface(recommend, 
    inputs=["text", "text"], 
    outputs="json",
    examples=[["50059918", "ALC"],
              ["712", "PAR"]]
)

iface.launch(port=8000)