"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.previous = 'ALC'

        self.initUI()

    def initUI(self):

        self.location_label = QLabel('Enter location:')
        self.location_input = QLineEdit()

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_location)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.location_label)
        self.layout.addWidget(self.location_input)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Travel Recommendation System')
        self.show()

    def submit_location(self):

        location = self.location_input.text()

        # Replace with your desired cities
        city_names = list(set(df['cityTo'])) 
        city_counts = user_df.filter(items=city_names).sum().sort_values(ascending=False)

        highest_city = city_counts.index[0]
        second_highest_city = city_counts.index[1]
        third_highest_city = city_counts.index[2]

        price_max_col = user_df.filter(like='PriceLvl_').idxmax(axis=1)
        activity_max_col = user_df.filter(['Beach', 'Nature', 'Cultural', 'Historical', 'Adventurous']).idxmax(axis=1)
        time_max_col = user_df.filter(['EarlyMorning', 'Morning', 'Noon', 'Afternoon', 'Evening', 'Night']).idxmax(axis=1)

        if i != 3:
            reco = model(location, self.previous, cities_dict[highest_city])
        elif i == 6:
            reco = model(location, self.previous, cities_dict[third_highest_city])
        else:
            reco = model(location, self.previous, cities_dict[second_highest_city])
        reco['local_departure'] = pd.to_datetime(reco['local_departure'])

        reco_filtered = reco[(reco['price'] >= price_ranges[str(price_max_col[0])][0]) & (reco['price'] <= price_ranges[str(price_max_col[0])][1])]
        reco_filtered2 = reco_filtered[(reco_filtered['local_departure'].dt.hour >= time_cols_dict[str(time_max_col[0])][0]) & (reco_filtered['local_departure'].dt.hour <= time_cols_dict[str(time_max_col[0])][1])]
        reco_filtered3 = reco_filtered2[reco_filtered2['category']== str(activity_max_col[0])]

        reco_others = reco[(reco['price'] < price_ranges[str(price_max_col[0])][0]) | (reco['price'] > price_ranges[str(price_max_col[0])][1])]
        reco_others2 = reco_filtered[(reco_filtered['local_departure'].dt.hour < time_cols_dict[str(time_max_col[0])][0]) | (reco_filtered['local_departure'].dt.hour > time_cols_dict[str(time_max_col[0])][1])]
        reco_others3 = reco_filtered2[reco_filtered2['category']!= str(activity_max_col[0])]

        reco_final = pd.concat([reco_filtered,reco_filtered2,reco_filtered3, reco_others,reco_others2,reco_others3])
        reco_final = reco_final.drop_duplicates(keep='first')

        self.previous = reco_final
        if reco_final.empty:
            # if no recommendation found, show message box
            QMessageBox.information(self, 'Sorry', 'No recommendations found for this location!')
        else:
            # create a new window to display the recommendations
            self.result_window = QWidget()
            self.result_layout = QVBoxLayout()

            # add a label for the recommendations
            self.result_label = QLabel('Here are your travel recommendations:')
            self.result_layout.addWidget(self.result_label)

            # add a label for each recommendation
            for index, row in reco_final.iterrows():
                recommendation = f"{row['cityTo']} - {row['price']} - {row['local_departure'].strftime('%Y-%m-%d %H:%M:%S')}"
                recommendation_label = QLabel(recommendation)
                self.result_layout.addWidget(recommendation_label)

            # add the layout to the window
            self.result_window.setLayout(self.result_layout)

            # show the window
            self.result_window.setGeometry(100, 100, 400, 200)
            self.result_window.setWindowTitle('Travel Recommendations')
            self.result_window.show()

"""