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


from Airbnb_data import Airbnb_data
# This should has a Text column that has all text we need
# id which has the airbnb id
# city of that airbnb should be there



def model_computations(field):
    def clean_text(text):
        text = "".join([word.lower() for word in text if word not in string.punctuation])
        tokens = re.findall('\S+', text)
        text = [ps.stem(word) for word in tokens if word not in stopwords.words('english')]
        text = [wn.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
        return text
    df = Airbnb_data().head(25000)
    ps = nltk.PorterStemmer()
    wn = nltk.WordNetLemmatizer()   
    df[field] = df[field].apply(lambda x: clean_text(x))
    df[field] = df[field].apply(lambda x: ' '.join(x))
    print('50 PERCENT')

    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df = 0, stop_words='english')
    tfidf_matrix = tf.fit_transform(df[field])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    df2 = df.reset_index()
    titles = pd.Series(df2[field])
    indices = pd.Series(df2.index, index = df2[field])
    return titles,indices, cosine_sim, df




def Airbnb_reco(location,previous,best_price,best_beds,best_People,best_reviews,titles,indices, cosine_sim, df):
    # best is previous best id of place
    # location is the most liked city
    #print(df)
    title = df.loc[(df['price'] >= best_price - 150) & (df['price'] <= best_price + 150) & (df['beds'] >= best_beds - 2) & (df['beds'] <= best_beds + 2)&(df['People'] >= best_People - 1.5) & (df['People'] <= best_People + 1.5)&(df['number_of_reviews'] >= best_reviews - 150) & (df['number_of_reviews'] <= best_reviews + 150), 'Text'].iloc[0]
    #print(title)
    idx = indices[title]  # Defining a variable with indices
    #print(idx)
    #print('-------')
    sim_scores = list(enumerate(cosine_sim[idx]))
    #print(sim_scores)
    #print('-------')

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #print(sim_scores)
    #print('-------')

    sim_scores = sim_scores[:8000]  # Taking the 30 most similar movies
    #print(sim_scores)
    #print('-------')

    movie_indices = [i[0] for i in sim_scores]
    #print(movie_indices)
    #print('-------')

    listy= list(titles.iloc[movie_indices][~titles.iloc[movie_indices].isin([title])]) # returns the title based on movie indices
    #print(len(listy))
    #print('-------')
    #listy = list(get_recommendations(df.loc[df['flyTo'] == location, 'Description'].iloc[0],titles,indices, cosine_sim))

    filtered_df = df[df['Text'].isin(listy)]
    #print(len(filtered_df))

    filtered_df = filtered_df[filtered_df['City']== location]
    #print('----------')
   # print(len(filtered_df))
    #print('----------')

    filtered_df = filtered_df[filtered_df['id'] != previous]
    
    return filtered_df