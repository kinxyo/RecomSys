# CinemaScope

![recom_sissy_demo](https://github.com/kinxyo/RecomSys/assets/90744941/8b0ce292-c0e4-4c7b-8fca-c4d0ae969cbe)

## About

**Have you ever grown tired of conventional films and just wished to discover something fresh yet similar to your preferences?**

_CinemaScope_ commits to solve this problem by utilizing machine learning. This webapp is developed to personalize movie recommendations, catering to unique user preferences. To take this a step further, we also provide recommendations by utilizing search history data to gain a comprehensive understanding of user preferences. This allows us to get bigger picture of one's taste. Our application is built using Flask.

## Theory

- In our _movie recommendation system_, we used **cosine similarity** to measure the similarity between different movies based on certain features. 
- These features could include aspects like genre, director, actors, and keywords from the movie's description. 
- Each movie is represented as a multi-dimensional vector of these features. The cosine similarity between any two movies is then calculated by taking the dot product of their feature vectors and dividing by the product of their magnitudes.
- This results in a similarity score between -1 and 1, where 1 means the movies are identical in terms of the features considered, 0 means they are completely dissimilar, and -1 means they are diametrically opposite.
- By calculating the cosine similarity between the movie a user has watched and all other movies in our database, we can recommend the movies with the highest similarity scores, thus personalizing the recommendations to the user's unique preferences.

![Frame 12](https://github.com/kinxyo/RecomSys/assets/90744941/979e90f7-2387-4708-ae06-cb3390e90a1c)

## How To Use

### Setup

#### Clone Repository

```bash
git clone https://github.com/kinxyo/RecomSys.git
```

#### Enter Virtual Env 

```bash
py -3 -m venv cinema
```

```bash
source cinema/scripts/activate
```

#### Install Requirements

```bash
pip install -r requirements.txt
```

#### Generate Artifacts (Output Model)

```bash
python ml.py
```

### Run

```bash
python wsgi.py
```

## Jupyter Notebook

You will also find a Jupyter Notebook in the repository. You can easily configure the tags and other algorithm-related stuff in it so you are able to generate your own artifacts by running the notebook.

The notebook will ask for selecting a kernel, select `cinema` from the dropdown menu. This will ensure that the notebook uses the same environment as the project.
Also, before running the notebook, make sure you have installed the following package:

```bash
pip install ipykernel
```

To convert the notebook to a python script, run the following command in the terminal:

```bash
pip install nbconvert
```

```bash
cd backend/ml
```

```bash
jupyter nbconvert --to script YourNotebook.ipynb
```

## Closing Remarks

Done as part of a college project.

You can learn more about **Cosine Similarity** [here](https://www.learndatasci.com/glossary/cosine-similarity/).

Find **Dataset** [here](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv).

## Project Poster

![recomsys-readme_poster](https://github.com/kinxyo/RecomSys/assets/90744941/30381925-9b0a-4325-847e-8af255789fe6)
