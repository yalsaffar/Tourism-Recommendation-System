from main import record
import gradio as gr
import pandas as pd
def demo_record(UserId , City, Category, Price_flight,Price_Air,Beds_air,People_air,Reviews_air, Category_place,Time_place, time, Indicator):
    UserId = int(UserId)
    Price_flight = float(Price_flight)
    Price_Air = float(Price_Air)
    Beds_air = float(Beds_air)
    People_air = float(People_air)
    Reviews_air = float(Reviews_air)
    Indicator = int(Indicator)
    user_df = pd.read_csv('../datasets/data_files/user_df.csv')
    pool_df = pd.read_csv('../datasets/data_files/pool_df.csv')
    record(UserId , City, Category, Price_flight,Price_Air,Beds_air,People_air,Reviews_air, Category_place,Time_place, time, user_df, pool_df, Indicator)
    return "Done.."
    
iface = gr.Interface(
    fn=demo_record, 
    inputs=[        gr.inputs.Textbox(label="User ID"),         gr.inputs.Textbox(label="City"),         gr.inputs.Textbox(label="Category"),         gr.inputs.Textbox(label="Price of Flight"),         gr.inputs.Textbox(label="Price of Airbnb"),         gr.inputs.Textbox(label="Beds in Airbnb"),         gr.inputs.Textbox(label="People in Airbnb"),         gr.inputs.Textbox(label="Reviews of Airbnb"),         gr.inputs.Textbox(label="Category of Place"),         gr.inputs.Textbox(label="Time of Place"),         gr.inputs.Textbox(label="Time"),         gr.inputs.Textbox(label="Indicator")    ],
    outputs="text" 
    
)

iface.launch(port=8000)