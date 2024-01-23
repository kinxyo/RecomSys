#!/usr/bin/env python
# coding: utf-8

# ## Content Based Recommender System

# In[158]:


import pandas as pd


# In[159]:


movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')


# In[160]:


movies.head(2)


# In[161]:


movies.shape


# In[162]:


credits.head()


# In[163]:


credits.shape


# In[164]:


movies = movies.merge(credits,on='title')


# In[165]:


movies.head(2)


# In[166]:


movies.shape


# In[167]:


# Keeping important columns for recommendation
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[168]:


movies.head(2)


# In[169]:


movies.shape


# In[170]:


movies.isnull().sum()


# In[171]:


movies.dropna(inplace=True)


# In[172]:


movies.isnull().sum()


# In[173]:


movies.shape


# In[174]:


movies.duplicated().sum()


# In[175]:


# handle genres

movies.iloc[0]['genres']


# In[ ]:





# In[176]:


import ast #for converting str to list

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L


# In[177]:


movies['genres'] = movies['genres'].apply(convert)


# In[178]:


movies.head()


# In[179]:


# handle keywords
movies.iloc[0]['keywords']


# In[180]:


movies['keywords'] = movies['keywords'].apply(convert)
movies.head()


# In[181]:


# handle cast
movies.iloc[0]['cast']


# In[182]:


# Here i am just keeping top 3 cast

def convert_cast(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L


# In[183]:


movies['cast'] = movies['cast'].apply(convert_cast)
movies.head()


# In[184]:


# handle crew

movies.iloc[0]['crew']


# In[185]:


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L


# In[186]:


movies['crew'] = movies['crew'].apply(fetch_director)


# In[187]:


movies.head()


# In[188]:


# handle overview (converting to list)

movies.iloc[0]['overview']


# In[189]:


movies['overview'] = movies['overview'].apply(lambda x:x.split())
movies.sample(4)


# In[190]:


movies.iloc[0]['overview']


# In[191]:


# now removing space like that 
'Anna Kendrick'
'AnnaKendrick'

def remove_space(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


# In[192]:


movies['cast'] = movies['cast'].apply(remove_space)


# In[193]:


movies.head()


# In[194]:


# Concatinate all
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']


# In[195]:


movies.head()


# In[196]:


movies.iloc[0]['tags']


# In[197]:


movies.head(5)


# In[198]:


# droping those extra columns
new_df = movies[['movie_id','title','tags']].copy()


# In[199]:


movies.head(5)


# In[200]:


new_df.head()


# In[201]:


# Converting list to str
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df.head()


# In[202]:


# Converting to lower case
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())


# In[203]:


new_df.iloc[0]['tags']


# In[204]:


# Removing corrupted and redundant data
index_names = new_df[new_df['movie_id'] == 113406].index
new_df.drop(index_names, inplace=True)
new_df = new_df.drop_duplicates(subset=['movie_id'])


# In[205]:


new_df.head()


# In[206]:


from nltk.stem import PorterStemmer


# In[207]:


ps = PorterStemmer()


# In[208]:


""" Stemming helps to reduce the dimentionality of the data
 and to focus on the meaning of the word rather than their form. """

def stems(text):
    T = []
    
    for i in text.split():
        T.append(ps.stem(i))
    
    return " ".join(T)


# In[209]:


new_df['tags'] = new_df['tags'].apply(stems)


# In[210]:


new_df.iloc[0]['tags']


# In[211]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[212]:


vector = cv.fit_transform(new_df['tags']).toarray()


# In[213]:


vector[0]


# In[214]:


vector.shape


# In[215]:


len(cv.get_feature_names_out())


# In[216]:


from sklearn.metrics.pairwise import cosine_similarity


# In[217]:


similarity = cosine_similarity(vector)


# In[218]:


similarity.shape


# In[219]:


new_df[new_df['title'] == 'The Lego Movie'].index[0]


# In[220]:


def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(new_df.iloc[i[0]].title)


# In[221]:


recommend('Spider-Man 2')


# In[222]:


movies.head(2)


# In[223]:


movies['overview'] = movies['overview'].apply(lambda x: " ".join(x))
movies['genres'] = movies['genres'].apply(lambda x: " ".join(x))
movies['cast'] = movies['cast'].apply(lambda x: " ".join(x))
movies['crew'] = movies['crew'].apply(lambda x: " ".join(x))



# In[224]:


movies.head(5)


# In[225]:


movies.head(2)


# In[226]:


import pickle
pickle.dump(new_df,open('out/tags.pkl','wb'))
pickle.dump(movies,open('out/movie_list.pkl','wb'))
pickle.dump(similarity,open('out/similarity.pkl','wb'))

