import pandas as pd
import nltk
import re
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel


from Flightss import flights_dataset




def model_computations():
    def clean_text(text):
        text = "".join([word.lower() for word in text if word not in string.punctuation])
        tokens = re.findall('\S+', text)
        text = [ps.stem(word) for word in tokens if word not in stopwords.words('english')]
        text = [wn.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
        return text
    df = flights_dataset()
    ps = nltk.PorterStemmer()
    wn = nltk.WordNetLemmatizer()   
    df['Description'] = df.Description.apply(lambda x: clean_text(x))
    df['Description'] = df['Description'].apply(lambda x: ' '.join(x))


    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df = 0, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['Description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    df2 = df.reset_index()
    titles = pd.Series(df2['Description'])
    indices = pd.Series(df2.index, index = df2['Description'])
    return titles,indices, cosine_sim, df




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