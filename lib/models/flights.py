def flights_reco(location,previous,best,titles,indices, cosine_sim, df):
    title = df.loc[df['flyTo'] == best, 'Description'].iloc[0]
    idx = indices[title]  # Defining a variable with indices
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1].all(), reverse=True)
    sim_scores = sim_scores  # Taking the 30 most similar movies
    movie_indices = [i[0] for i in sim_scores]
    listy= list(titles.iloc[movie_indices][~titles.iloc[movie_indices].isin([title])]) # returns the title based on movie indices

    #listy = list(get_recommendations(df.loc[df['flyTo'] == location, 'Description'].iloc[0],titles,indices, cosine_sim))

    filtered_df = df[df['Description'].isin(listy)]
    filtered_df = filtered_df[filtered_df['flyFrom']== location]
    if previous != 0:

        filtered_df = filtered_df[filtered_df['flyTo'] != previous]
    
    return filtered_df