# IMPORTS
from flask import Flask, render_template
from backend.functions import *

app = Flask(__name__, template_folder="frontend")

@app.route('/')
def Home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


# app.run(debug=True)

""" 
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
        st.image(recommended_movie_posters[4]) """