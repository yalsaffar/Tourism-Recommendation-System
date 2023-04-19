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

from Places_data import Places_data
# This should has a Text column that has all text we need
# id which has the placce id
# city of that place should be there

def model_computations():
    """
    Preprocesses the text data and computes the cosine similarity matrix for the Airbnb places dataset.

    Returns:
    - titles: pd.Series containing the preprocessed text for each place
    - indices: pd.Series containing the index of each place in the dataset
    - cosine_sim: numpy array representing the cosine similarity matrix of the preprocessed text
    - df: pd.DataFrame containing the preprocessed Airbnb dataset
    """

    def clean_text(text):
        text = "".join([word.lower() for word in text if word not in string.punctuation])
        tokens = re.findall('\S+', text)
        text = [ps.stem(word) for word in tokens if word not in stopwords.words('english')]
        text = [wn.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
        return text
    df = Places_data()
    df = df.rename(columns={'text': 'Text'})
    ps = nltk.PorterStemmer()
    wn = nltk.WordNetLemmatizer()   
    df['Text'] = df['Text'].apply(lambda x: clean_text(x))
    df['Text'] = df['Text'].apply(lambda x: ' '.join(x))


    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df = 0, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['Text'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    df2 = df.reset_index()
    titles = pd.Series(df2['Text'])
    indices = pd.Series(df2.index, index = df2['Text'])
    return titles,indices, cosine_sim, df



def Places_reco(city, cosine_sim, place_df, previous_place_id):
    """
    Recommends places in a given city based on the similarity of their attributes to the previous recommended place.
    
    Args:
    city (str): The name of the city for which recommendations are requested.
    cosine_sim (numpy.ndarray): The cosine similarity matrix of the place dataset.
    place_df (pandas.DataFrame): The dataset of places containing their attributes.
    previous_place_id (int): The ID of the previously recommended place.
    
    Returns:
    pandas.DataFrame: A filtered dataset of recommended places in the specified city based on the similarity of their attributes to the previous recommended place.
    
    Raises:
    ValueError: If the previous_place_id is not found in the dataset.
    """

    if previous_place_id not in place_df['place_id'].values:
        raise ValueError(f"Invalid previous_place_id: {previous_place_id}")

    if previous_place_id != 0:
        idx = place_df.index.get_loc(place_df[place_df['place_id'] == previous_place_id].index[0])
    else:
        idx = place_df.index.get_loc(place_df[place_df['city'] == city].index[0])

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:]

    place_indices = [i[0] for i in sim_scores]
    filtered_df = place_df.iloc[place_indices]
    filtered_df = filtered_df[filtered_df['city'] == city]

    if previous_place_id != 0:
        filtered_df = filtered_df[filtered_df['place_id'] != previous_place_id]

    return filtered_df