import pandas as pd




def Airbnb_data():
    listing_df_madrid = pd.read_csv("data_files/listings_mad.csv")
    review_df_madrid = pd.read_csv("data_files/reviews_mad.csv")
    listing_df_barcelona = pd.read_csv("data_files/listings_bar.csv")
    review_df_barcelona = pd.read_csv("data_files/reviews_bar.csv")
    listing_df_girona = pd.read_csv("data_files/listings_gir.csv")
    review_df_girona = pd.read_csv("data_files/reviews_gir.csv")
    listing_df_malaga = pd.read_csv("data_files/listings_mal.csv")
    review_df_malaga = pd.read_csv("data_files/reviews_mal.csv")
    listing_df_mallorca = pd.read_csv("data_files/listings_mallo.csv")
    review_df_mallorca = pd.read_csv("data_files/reviews_mallo.csv")
    listing_df_menorca = pd.read_csv("data_files/listings_meno.csv")
    review_df_menorca = pd.read_csv("data_files/reviews_meno.csv")
    listing_df_sevilla = pd.read_csv("data_files/listings_sev.csv")
    review_df_sevilla = pd.read_csv("data_files/reviews_sev.csv")
    cols_to_remove = ['bathrooms', 'calendar_updated', 'host_neighbourhood', 'host_about',
                  'neighbourhood', 'neighborhood_overview', 'host_location', 'review_scores_value',
                  'review_scores_location', 'review_scores_communication', 'review_scores_checkin',
                  'review_scores_cleanliness', 'review_scores_accuracy', 'reviews_per_month',
                  'first_review', 'review_scores_rating', 'last_review', 'host_response_time',
                  'host_response_rate', 'host_acceptance_rate', 'bedrooms', 'license',
                  'picture_url', 'host_id', 'host_url', 'host_name', 'host_since',
                  'host_thumbnail_url', 'host_picture_url', 'host_listings_count',
                  'host_total_listings_count', 'host_verifications', 'host_has_profile_pic',
                  'host_identity_verified', 'scrape_id', 'last_scraped', 'source','neighbourhood_group_cleansed']

    # Remove the specified columns from the dataframe
    listing_df_madrid = listing_df_madrid.drop(cols_to_remove, axis=1)
    listing_df_barcelona = listing_df_barcelona.drop(cols_to_remove, axis=1)
    listing_df_girona = listing_df_girona.drop(cols_to_remove, axis=1)
    listing_df_malaga = listing_df_malaga.drop(cols_to_remove, axis=1)
    listing_df_mallorca = listing_df_mallorca.drop(cols_to_remove, axis=1)
    listing_df_menorca = listing_df_menorca.drop(cols_to_remove, axis=1)
    listing_df_sevilla = listing_df_sevilla.drop(cols_to_remove, axis=1)
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
    merged_dataset_madrid = pd.merge(listing_df_madrid, grouped_dataset_madrid, on='id',how='inner')

    merged_dataset_barcelona = pd.merge(listing_df_barcelona, grouped_dataset_barcelona, on='id',how='inner')

    merged_dataset_girona = pd.merge(listing_df_girona, grouped_dataset_girona, on='id',how='inner')

    merged_dataset_malaga = pd.merge(listing_df_malaga, grouped_dataset_malaga, on='id',how='inner')

    merged_dataset_mallorca = pd.merge(listing_df_mallorca, grouped_dataset_mallorca, on='id',how='inner')

    merged_dataset_menorca = pd.merge(listing_df_menorca, grouped_dataset_menorca, on='id',how='inner')

    merged_dataset_sevilla = pd.merge(listing_df_sevilla, grouped_dataset_sevilla, on='id',how='inner')
    spain_df = pd.concat([merged_dataset_madrid, merged_dataset_barcelona,merged_dataset_girona,merged_dataset_malaga,
                     merged_dataset_mallorca,merged_dataset_menorca,merged_dataset_sevilla])
    spain_df=spain_df.reset_index()
    return spain_df