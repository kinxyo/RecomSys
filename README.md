# Movie Recommendation System

## About
Ever got bored of mainstream cinema and just wanted to watch some new stuff that still resemebles your taste?
We provide a machine learning solution for it.<br>
This Streamlit webapp is designed to suggest variety of movies that align with a user's choice in films.
All you have to do is select the movie you like, and we'll recommend you with bunch of films that will match your taste.<br>
imghere.
To take it one-step further, we also provide recommendations based on your _search history_ so that we get an even bigger picture of your taste, and are able to provide you much better suggestions.

### Concept
- Our product is powered by machine learning. 
- Data pulled from the dataset is placed into a numpy array to achieve a vector form.
- We have trained our ml model on the **Cosine Similarity** metric, which allows it to measure similiarity between vectors.
- Once we have our vectors ready, cosine_similarity() is called on them to calculate the cosine similarity between the two vectors.
- Value of the metric lies between 0 & 1. The closer it's to 1, the more similiarity there appear to be.

#### Learn More
[Cosine Similarity](https://www.learndatasci.com/glossary/cosine-similarity/)
<br>
[Dataset Used](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## How To Use

### Setup
#### Clone Repository
```
https://github.com/kinxyo/RecomSys.git
```
#### Create & Activate Conda Environment
```
conda create -n movie python=3.7.10 -y
```
```
source activate movie
```
#### Install Requirements
```
pip install -r requirements.txt
```
#### Generate Artifacts (Model Output)
_Run **ml_recommendation.ipynb** file_

### Run
```
streamlit run app.py
```

## Closing Remarks
This project was done as part of a small college project. <br>
We used Streamlit so that we could focus on machine learning part without worrying about the frontend.
Currently our system is content-based but we're very much inclined to push to a hybrid model (Content-based + Collaborative filtering).
We are also looking to upgrade to Flask to improve the frotend.
### Team
- Gitansh
- Om
- Kinjalk 
- Himanshu