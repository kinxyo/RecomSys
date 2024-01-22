# IMPORTS
import pickle
import requests

# GLOBAL VARIABLES
movies = pickle.load(open('backend/ml/out/tags.pkl','rb'))
movies = movies.drop_duplicates(subset=['movie_id'])
cinema = pickle.load(open('backend/ml/out/movie_list.pkl','rb'))
similarity = pickle.load(open('backend/ml/out/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    try:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        print(f"No poster found for {get_name(movie_id)}")

def search_movie(search_term):
    # Return a DataFrame of movies that match the search term
    matching_movies = movies[movies['title'].str.contains(search_term, case=False)]
    return matching_movies

def recommend(movie_id):
    movie_df = movies[movies['movie_id'] == movie_id]
    movie_searched = movie_df.iloc[0].title
    if not movie_df.empty:
        index = movie_df.index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        recommended_movie_ids = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_ids.append(movies.iloc[i[0]].movie_id)
        return  recommended_movie_names,recommended_movie_posters, recommended_movie_ids,  movie_searched
    else:
        print(f"Sorry, we don't have any recommendations for you for {movie_df.iloc[0].title}")
        return
    
def recommend_from_history(movie):
    movie_df = movies[movies['title'] == movie]
    if not movie_df.empty:
        index = movie_df.index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names,recommended_movie_posters
    else:
        print(f"No movie found with title {movie}")
        return
    
def retrieve_movie(movie_id):
    movie_df = cinema[cinema['movie_id'] == movie_id]
    if not movie_df.empty:
        poster = fetch_poster(movie_id)
        
        print("error sus --> ", movie_df.iloc[0])

        return {'name': movie_df.iloc[0].title, 'thumbnail': poster, 'synopsis': movie_df.iloc[0].overview, 'genre': movie_df.iloc[0].genres, 'cast': movie_df.iloc[0].cast}

    else:
        print(f"No movie found with id {movie_id}")
        return
    
def get_name(id):
    movie_df = movies[movies['movie_id'] == id]
    if not movie_df.empty:
        return movie_df.iloc[0].title
    else:
        print(f"No movie found with id {id}")
        return