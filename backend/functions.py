# IMPORTS
import pickle
from requests import Session
from cachetools import cached, TTLCache
from concurrent.futures import ThreadPoolExecutor

# GLOBAL VARIABLES
movies = pickle.load(open('backend/ml/out/cinema.pkl','rb'))
metric = pickle.load(open('backend/ml/out/metric.pkl','rb'))


# Create a session object
session = Session()

# Create a cache
cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    try:
        data = session.get(url)
        data.raise_for_status()  # Raises a HTTPError if the response status code is 4xx or 5xx
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except Exception as e:
        print(f"Error fetching poster for {get_name(movie_id)}: {e}")
        return

def search_movie_by_name(keyword):
    # Return a DataFrame of movies that match the search term
    matching_movies = movies[movies['title'].str.contains(keyword, case=False)]
    return matching_movies

""" ADD MORE FILTERS FOR SEARCH """

def recommend(movie_df):
    index = movie_df.index[0]
    distances = sorted(list(enumerate(metric[index])), reverse=True, key=lambda x: x[1])
    recom_names = []
    recom_posters = []
    recom_ids = []

    with ThreadPoolExecutor() as executor:
        for i in distances[1:6]:
            movie_row = movies.iloc[i[0]]
            movie_id = movie_row.movie_id
            poster_future = executor.submit(fetch_poster, movie_id)
            recom_posters.append(poster_future)
            recom_names.append(movie_row.title)
            recom_ids.append(movie_id)
    # Wait for all poster fetches to complete and get the results
    recom_posters = [future.result() for future in recom_posters]
    return recom_names, recom_posters, recom_ids

def get_recommendations(movie_id):
    movie_df = get_dataframe(movie_id)
    movie_searched = get_name(movie_id)
    if not movie_df.empty:
        return recommend(movie_df)
    else:
        print(f"Sorry, we don't have any recommendations for you for {movie_searched}")
        return
    
def get_all(movie_id):
    movie_df = get_dataframe(movie_id)
    if not movie_df.empty:
        return {'name': movie_df.iloc[0].title, 'thumbnail': fetch_poster(movie_id), 'synopsis': movie_df.iloc[0].overview, 'genre': movie_df.iloc[0].genres, 'cast': movie_df.iloc[0].cast}

    else:
        print(f"No movie found with id {movie_id}")
        return    

def get_name(id):
    movie_df = get_dataframe(id)
    if not movie_df.empty:
        return movie_df.iloc[0].title
    else:
        print(f"No movie found with id {id}")
        return
    
def get_dataframe(id):
    movie_df = movies[movies['movie_id'] == id]
    return movie_df