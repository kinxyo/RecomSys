# IMPORTS
from email.mime import base
from numpy import full
import pickle
import streamlit as st
import requests
    
# FUNCTIONS
def save_search(movie):
    with open("archive/history.txt","r") as check:
        content = check.read()
        if movie in content:
            pass
        else:
            with open('archive/history.txt','a') as file:
                file.write(f"{movie}\n")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


# GLOBAL VARIABLES
movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))


# BODY
st.title('Movie Recommendation System')

# SECTION -- Based on Search History
st.header("Based on Search History")
based_list = []
with open("archive/history.txt","r") as file:
    films = file.readlines()
    for title in films:
        new_list = title.split("\n")
        based_list.insert(0, new_list[0])
    
    slot = st.columns(5)
    for i in range(5):
        based_movie,based_poster = recommend(based_list[i])
        with slot[i]:
            st.text(based_movie[0])
            st.image(based_poster[0])


# SECTION -- Based on Manual Search
st.header('Manual Searching')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select Movie:",
    movie_list
)

if st.button('Recommend'):
    save_search(selected_movie)
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])