import pandas as pd
#from mtranslate import translate
from langdetect import detect, LangDetectException
from nrclex import NRCLex
import pandas as pd
def is_english(comment):
    try:
        return detect(comment) == 'en'
    except LangDetectException:
        return False

def analyze_emotions(comment):
    """
    Analyzes the emotions expressed in a given comment and returns the affect frequencies.

    Parameters:
    comment (str): The comment to analyze.

    Returns:
    dict: A dictionary containing the frequencies of each affect in the comment. The keys are
          the six basic emotions (anger, fear, anticipation, trust, surprise, sadness) and
          valence (positive or negative), and the values are the frequencies of each affect in
          the comment, normalized to a scale of 0 to 1.
    """


    emotion = NRCLex(comment)
    #print('-')
    return emotion.affect_frequencies

def Airbnb_data():
    """
      Reads in Airbnb listing and review data for several cities in Spain, processes the data to remove unnecessary columns 
      and filter for relevant listings and reviews, performs sentiment analysis on the reviews to extract emotional frequencies, 
      and returns a cleaned and analyzed DataFrame containing information on the top 1500 listings in each city based on number 
      of reviews, along with additional columns for emotion frequencies and price.

      Returns:
      DataFrame: A cleaned and analyzed DataFrame containing information on the top 1500 listings in each city based on number 
                of reviews, along with additional columns for emotion frequencies and price.
    """

    listing_df_madrid = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/listings_mad.csv")
    review_df_madrid = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/reviews_mad.csv")
    listing_df_barcelona = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/listings_bar.csv")
    review_df_barcelona = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/reviews_bar.csv")
    listing_df_girona = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/listings_gir.csv")
    review_df_girona = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/reviews_gir.csv")
    listing_df_malaga = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/listings_mal.csv")
    review_df_malaga = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/reviews_mal.csv")
    listing_df_mallorca = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/listings_mallo.csv")
    review_df_mallorca = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/reviews_mallo.csv")
    listing_df_menorca = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/listings_meno.csv")
    review_df_menorca = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/reviews_meno.csv")
    listing_df_sevilla = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/listings_sev.csv")
    review_df_sevilla = pd.read_csv("/home/runner/work/Tourism-Recommendation-System/Tourism-Recommendation-System/lib/datasets/data_files/reviews_sev.csv")
    cols_to_remove = ['bathrooms', 'calendar_updated', 'host_neighbourhood', 'host_about',
                  'neighbourhood', 'neighborhood_overview', 'host_location', 'review_scores_value',
                  'review_scores_location', 'review_scores_communication', 'review_scores_checkin',
                  'review_scores_cleanliness', 'review_scores_accuracy', 'reviews_per_month',
                  'first_review', 'review_scores_rating', 'last_review', 'host_response_time',
                  'host_response_rate', 'host_acceptance_rate', 'bedrooms', 'license',
                  'picture_url', 'host_id', 'host_url', 'host_name', 'host_since',
                  'host_thumbnail_url', 'host_picture_url', 'host_listings_count',
                  'host_total_listings_count', 'host_verifications', 'host_has_profile_pic',
                  'host_identity_verified', 'scrape_id', 'last_scraped', 'source','neighbourhood_group_cleansed','calendar_last_scraped','number_of_reviews_ltm', 'number_of_reviews_l30d','availability_30', 'availability_60', 'availability_90',
       'availability_365', 'calendar_last_scraped','calculated_host_listings_count',
       'calculated_host_listings_count_entire_homes',
       'calculated_host_listings_count_private_rooms',
       'calculated_host_listings_count_shared_rooms',
       'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm']
    #-------------------------------------------
    listing_df_madrid.sort_values('number_of_reviews',ascending=False).iloc[:1500]
    listing_df_barcelona.sort_values('number_of_reviews',ascending=False).iloc[:1500]
    listing_df_girona.sort_values('number_of_reviews',ascending=False).iloc[:1500]
    listing_df_mallorca.sort_values('number_of_reviews',ascending=False).iloc[:1500]
    listing_df_menorca.sort_values('number_of_reviews',ascending=False).iloc[:1500]
    listing_df_sevilla.sort_values('number_of_reviews',ascending=False).iloc[:1500]
    listing_df_malaga.sort_values('number_of_reviews',ascending=False).iloc[:1500]
    #----------------------------------------------
    review_df_madrid.loc[review_df_madrid['comments'].apply(lambda x: isinstance(x, str) and len(x.split()) > 15)]
    review_df_barcelona.loc[review_df_barcelona['comments'].apply(lambda x: isinstance(x, str) and len(x.split()) > 15)]
    review_df_girona.loc[review_df_girona['comments'].apply(lambda x: isinstance(x, str) and len(x.split()) > 15)]
    review_df_malaga.loc[review_df_malaga['comments'].apply(lambda x: isinstance(x, str) and len(x.split()) > 15)]
    review_df_mallorca.loc[review_df_mallorca['comments'].apply(lambda x: isinstance(x, str) and len(x.split()) > 15)]
    review_df_menorca.loc[review_df_menorca['comments'].apply(lambda x: isinstance(x, str) and len(x.split()) > 15)]
    review_df_sevilla.loc[review_df_sevilla['comments'].apply(lambda x: isinstance(x, str) and len(x.split()) > 15)]

    #--------------------------------------------
    listing_df_madrid = listing_df_madrid.assign(City='Madrid')
    listing_df_barcelona = listing_df_barcelona.assign(City='Barcelona')
    listing_df_girona = listing_df_girona.assign(City='Girona')
    listing_df_malaga = listing_df_malaga.assign(City='Malaga')
    listing_df_mallorca = listing_df_mallorca.assign(City='Mallorca')
    listing_df_menorca = listing_df_menorca.assign(City='Menorca')
    listing_df_sevilla = listing_df_sevilla.assign(City='Sevilla')
    #---------------------------------------------------
    # Remove the specified columns from the dataframe
    listing_df_madrid = listing_df_madrid.drop(cols_to_remove, axis=1)
    listing_df_barcelona = listing_df_barcelona.drop(cols_to_remove, axis=1)
    listing_df_girona = listing_df_girona.drop(cols_to_remove, axis=1)
    listing_df_malaga = listing_df_malaga.drop(cols_to_remove, axis=1)
    listing_df_mallorca = listing_df_mallorca.drop(cols_to_remove, axis=1)
    listing_df_menorca = listing_df_menorca.drop(cols_to_remove, axis=1)
    listing_df_sevilla = listing_df_sevilla.drop(cols_to_remove, axis=1)
    #------------------------------------------------
    listing_df_madrid.dropna(inplace=True)
    review_df_madrid.dropna(inplace=True)

    listing_df_barcelona.dropna(inplace=True)
    review_df_barcelona.dropna(inplace=True)

    listing_df_girona.dropna(inplace=True)
    review_df_girona.dropna(inplace=True)

    listing_df_malaga.dropna(inplace=True)
    review_df_malaga.dropna(inplace=True)

    listing_df_mallorca.dropna(inplace=True)
    review_df_mallorca.dropna(inplace=True)

    listing_df_menorca.dropna(inplace=True)
    review_df_menorca.dropna(inplace=True)

    listing_df_sevilla.dropna(inplace=True)
    review_df_sevilla.dropna(inplace=True)
    #-------------------------------------------------
    #print('translating...')
    #review_df_madrid['comments'] = review_df_madrid['comments'].apply(lambda x: translate(x, 'en'))
    #review_df_barcelona['comments'] = review_df_barcelona['comments'].apply(lambda x: translate(x, 'en'))
    #review_df_girona['comments'] = review_df_girona['comments'].apply(lambda x: translate(x, 'en'))
    #review_df_malaga['comments'] = review_df_malaga['comments'].apply(lambda x: translate(x, 'en'))
    #review_df_mallorca['comments'] = review_df_mallorca['comments'].apply(lambda x: translate(x, 'en'))
    #review_df_menorca['comments'] = review_df_menorca['comments'].apply(lambda x: translate(x, 'en'))
    #review_df_sevilla['comments'] = review_df_sevilla['comments'].apply(lambda x: translate(x, 'en'))
    #print('Done translating...')
    #--------------------------------------------------
 # Get the latest reviews for each listing_id
    review_df_madrid = review_df_madrid.sort_values('date', ascending=False).groupby('listing_id').head()
    review_df_barcelona = review_df_barcelona.sort_values('date', ascending=False).groupby('listing_id').head()
    review_df_girona = review_df_girona.sort_values('date', ascending=False).groupby('listing_id').head()
    review_df_malaga = review_df_malaga.sort_values('date', ascending=False).groupby('listing_id').head()
    review_df_mallorca = review_df_mallorca.sort_values('date', ascending=False).groupby('listing_id').head()
    review_df_menorca = review_df_menorca.sort_values('date', ascending=False).groupby('listing_id').head()
    review_df_sevilla = review_df_sevilla.sort_values('date', ascending=False).groupby('listing_id').head()

    #print('Detecting lang...')

    #review_df_madrid = review_df_madrid[review_df_madrid['comments'].apply(is_english)]
    #review_df_barcelona = review_df_barcelona[review_df_barcelona['comments'].apply(is_english)]
    #review_df_girona = review_df_girona[review_df_girona['comments'].apply(is_english)]
    #review_df_malaga = review_df_malaga[review_df_malaga['comments'].apply(is_english)]
    #review_df_mallorca = review_df_mallorca[review_df_mallorca['comments'].apply(is_english)]
    #review_df_menorca = review_df_menorca[review_df_menorca['comments'].apply(is_english)]
    #review_df_sevilla = review_df_sevilla[review_df_sevilla['comments'].apply(is_english)]

    #print('Done detecting...')
    #---------------------------------------------------------





    grouped_dataset_madrid = review_df_madrid.astype({'comments': str}).groupby('listing_id')['comments'].apply(' '.join).reset_index()

    grouped_dataset_barcelona = review_df_barcelona.astype({'comments': str}).groupby('listing_id')['comments'].apply(' '.join).reset_index()

    grouped_dataset_girona = review_df_girona.astype({'comments': str}).groupby('listing_id')['comments'].apply(' '.join).reset_index()

    grouped_dataset_malaga = review_df_malaga.astype({'comments': str}).groupby('listing_id')['comments'].apply(' '.join).reset_index()

    grouped_dataset_mallorca = review_df_mallorca.astype({'comments': str}).groupby('listing_id')['comments'].apply(' '.join).reset_index()

    grouped_dataset_menorca = review_df_menorca.astype({'comments': str}).groupby('listing_id')['comments'].apply(' '.join).reset_index()

    grouped_dataset_sevilla = review_df_sevilla.astype({'comments': str}).groupby('listing_id')['comments'].apply(' '.join).reset_index()
   
    grouped_dataset_madrid = grouped_dataset_madrid.rename(columns={'listing_id': 'id'})

    grouped_dataset_barcelona = grouped_dataset_barcelona.rename(columns={'listing_id': 'id'})

    grouped_dataset_girona = grouped_dataset_girona.rename(columns={'listing_id': 'id'})

    grouped_dataset_malaga = grouped_dataset_malaga.rename(columns={'listing_id': 'id'})

    grouped_dataset_mallorca = grouped_dataset_mallorca.rename(columns={'listing_id': 'id'})

    grouped_dataset_menorca = grouped_dataset_menorca.rename(columns={'listing_id': 'id'})

    grouped_dataset_sevilla = grouped_dataset_sevilla.rename(columns={'listing_id': 'id'})
    #-------------------------------------------------------
    merged_dataset_madrid = pd.merge(listing_df_madrid, grouped_dataset_madrid, on='id',how='inner')
    merged_dataset_barcelona = pd.merge(listing_df_barcelona, grouped_dataset_barcelona, on='id',how='inner')
    merged_dataset_girona = pd.merge(listing_df_girona, grouped_dataset_girona, on='id',how='inner')
    merged_dataset_malaga = pd.merge(listing_df_malaga, grouped_dataset_malaga, on='id',how='inner')
    merged_dataset_mallorca = pd.merge(listing_df_mallorca, grouped_dataset_mallorca, on='id',how='inner')
    merged_dataset_menorca = pd.merge(listing_df_menorca, grouped_dataset_menorca, on='id',how='inner')
    merged_dataset_sevilla = pd.merge(listing_df_sevilla, grouped_dataset_sevilla, on='id',how='inner')
    #----------------------------------------------------------
    spain_df = pd.concat([merged_dataset_madrid, merged_dataset_barcelona,merged_dataset_girona,merged_dataset_malaga,
                     merged_dataset_mallorca,merged_dataset_menorca,merged_dataset_sevilla])
    spain_df=spain_df.reset_index()
    #----------------------------------------------------------
    spain_df['Text'] = spain_df['description'] + spain_df['name'] + spain_df['amenities']
    spain_df['People'] = spain_df['accommodates'] / spain_df['beds']
    spain_df['Min_Duration'] = spain_df['minimum__maximum__nights'] - spain_df['minimum_minimum_nights'] 
    spain_df = spain_df.drop('index',axis=1)
    spain_df = spain_df[spain_df['has_availability']=='t']
    spain_df = spain_df.groupby('name').first()
    unique_cities = spain_df['City'].unique()

      # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

      # Loop through the unique cities and extract the 2000 rows with the highest 'number_of_reviews' values for each city
    for city in unique_cities:
      city_df = spain_df.loc[spain_df['City'] == city, :].nlargest(1500, 'number_of_reviews')
      result_df = pd.concat([result_df, city_df], axis=0)

      # Reset the index of the resulting DataFrame
      result_df = result_df.reset_index(drop=True)
    
    #print(result_df.columns)
    

    # Define a function to analyze emotions in each comment
    

    # Apply the emotion analysis to all comments and store the results in a new column
    result_df['Emotion_Frequencies'] = result_df['comments'].apply(analyze_emotions)
    #print('50per done')
    # Extract the frequency values for each emotion into separate columns
    emotions = ['fear', 'anger', 'anticip', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust', 'joy']
    for emotion in emotions:
        result_df[emotion] = result_df['Emotion_Frequencies'].apply(lambda x: x[emotion])

    # Drop the 'Emotion_Frequencies' column
    result_df = result_df.drop('Emotion_Frequencies', axis=1)
    #print(result_df.columns)
    result_df['price'] = result_df['price'].str.replace('$', '').str.replace(',', '',regex=False).str.replace('.', '', regex=False).astype(int)
    result_df['price'] = result_df['price']/100
    return result_df
