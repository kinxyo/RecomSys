#!/usr/bin/env python
# coding: utf-8

# ## Content Based Recommender System

# In[1]:


import pandas as pd


# In[2]:


movies = pd.read_csv('backend/ml/data/tmdb_5000_movies.csv')
credits = pd.read_csv('backend/mldata/tmdb_5000_credits.csv')


# In[3]:


movies.head(2)


# In[4]:


movies.shape


# In[5]:


credits.head()


# In[6]:


credits.shape


# In[7]:


movies = movies.merge(credits,on='title')


# In[8]:


movies.head(2)


# In[9]:


movies.shape


# In[10]:


# Keeping important columns for recommendation
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[11]:


movies.head(2)


# In[12]:


movies.shape


# In[13]:


movies.isnull().sum()


# In[14]:


movies.dropna(inplace=True)


# In[15]:


movies.isnull().sum()


# In[16]:


movies.shape


# In[17]:


movies.duplicated().sum()


# In[18]:


# handle genres

movies.iloc[0]['genres']


# In[ ]:





# In[19]:


import ast #for converting str to list

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L


# In[20]:


movies['genres'] = movies['genres'].apply(convert)


# In[21]:


movies.head()


# In[22]:


# handle keywords
movies.iloc[0]['keywords']


# In[23]:


movies['keywords'] = movies['keywords'].apply(convert)
movies.head()


# In[24]:


# handle cast
movies.iloc[0]['cast']


# In[25]:


# only keeping top 3 cast members

def convert_cast(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L


# In[26]:


movies['cast'] = movies['cast'].apply(convert_cast)
movies.head()


# In[27]:


# handle crew

movies.iloc[0]['crew']


# In[28]:


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L


# In[29]:


movies['crew'] = movies['crew'].apply(fetch_director)


# In[30]:


movies.head()


# In[31]:


# handle overview (converting to list because we will use count vectorizer)

movies.iloc[0]['overview']


# In[32]:


movies['overview'] = movies['overview'].apply(lambda x:x.split())
movies.sample(4)


# In[33]:


movies.iloc[0]['overview']


# In[34]:


# removing space
'Bradley Cooper'
'BradleyCooper'

def remove_space(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


# In[35]:


movies['cast'] = movies['cast'].apply(remove_space)


# In[36]:


movies.head()


# In[37]:


# Concatinate all
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']


# In[38]:


movies.head()


# In[39]:


movies.iloc[0]['tags']


# In[40]:


movies.head(5)


# In[41]:


movies.head()


# In[42]:


# Converting list to str
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))
movies.head()


# In[43]:


# Converting to lower case
movies['tags'] = movies['tags'].apply(lambda x:x.lower())


# In[44]:


movies.iloc[0]['tags']


# In[45]:


# Removing corrupted and redundant data
index_names = movies[movies['movie_id'] == 113406].index
movies.drop(index_names, inplace=True)
index_names = movies[movies['movie_id'] == 112430].index
movies.drop(index_names, inplace=True)
index_names = movies[movies['movie_id'] == 181940].index
movies.drop(index_names, inplace=True)
movies = movies.drop_duplicates(subset=['movie_id'])


# In[46]:


movies.head()


# In[47]:


from nltk.stem import PorterStemmer


# In[48]:


ps = PorterStemmer()


# In[49]:


""" Stemming helps to reduce the dimentionality of the data
 and to focus on the meaning of the word rather than their form. """

def stems(text):
    T = []
    
    for i in text.split():
        T.append(ps.stem(i))
    
    return " ".join(T)


# In[50]:


movies['tags'] = movies['tags'].apply(stems)


# In[51]:


movies.iloc[0]['tags']


# In[52]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[53]:


vector = cv.fit_transform(movies['tags']).toarray()


# In[54]:


vector[0]


# In[55]:


vector.shape


# In[56]:


len(cv.get_feature_names_out())


# In[57]:


from sklearn.metrics.pairwise import cosine_similarity


# In[58]:


similarity = cosine_similarity(vector)


# In[59]:


similarity.shape


# In[60]:


movies[movies['title'] == 'The Lego Movie'].index[0]


# In[61]:


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(movies.iloc[i[0]].title)


# In[62]:


recommend('Spider-Man 2')


# In[63]:


movies.head(2)


# In[64]:


movies['overview'] = movies['overview'].apply(lambda x: " ".join(x))
movies['genres'] = movies['genres'].apply(lambda x: " ".join(x))
movies['cast'] = movies['cast'].apply(lambda x: " ".join(x))
movies['crew'] = movies['crew'].apply(lambda x: " ".join(x))



# In[65]:


movies.head(5)


# In[66]:


import pickle
pickle.dump(movies,open('backend/ml/out/cinema.pkl','wb'))
pickle.dump(similarity,open('backend/ml/out/metric.pkl','wb'))