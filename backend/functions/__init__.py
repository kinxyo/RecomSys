# IMPORTS
import pickle
import requests

# GLOBAL VARIABLES
movies = pickle.load(open('././ml/output/movie_list.pkl','rb'))
similarity = pickle.load(open('././ml/output/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    print(movie)
    # index = movies[movies['title'] == movie].index[0]
    movie_df = movies[movies['title'] == movie]
    if not movie_df.empty:
        index = movie_df.index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names,recommended_movie_posters
    else:
        print(f"No movie found with title {movie}")
        return