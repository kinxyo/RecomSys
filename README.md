# CinemaScope

## About
Have you ever grown tired of conventional films and just wished to discover something fresh yet similar to your preferences?
Well, this is a _machine learning_ solution for it.<br>
This webapp is developed to personalize movie recommendations, catering to unique user preferences.<br>
All you have to do is, simply choose a movie that you enjoy and we will immediately suggest a collection of films that suit your taste.
<br>
<br>
![recomsys](https://github.com/kinxyo/RecomSys/assets/90744941/07484206-dfcb-4ea9-babb-0edbc7bd1ab2)
<br>
<br>
To take this one-step further, we have enhanced our recommendations by utilizing search history data to gain a comprehensive understanding of user preferences. This allows us to get bigger picture of one's taste.
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
python app.py
```

## Closing Remarks
We've remade our previous Streamlit app in Flask to expand upon functionalities and provide a more mordern touch to the UI.
<br>
### TEAM
- Kinjalk 
- [Gitansh](https://github.com/Gitansh-Agarwal)
- [Om](https://github.com/Ashu-Pablo) 
- [Himanshu](https://github.com/xendai66)
