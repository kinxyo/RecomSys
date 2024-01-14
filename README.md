# Movie Recommendation System

## About
Have you ever grown tired of conventional films and just wished to discover something fresh yet similar to your preferences?
We provide a machine learning solution for it.<br>
This Streamlit webapp is developed to personalize movie recommendations, catering to unique user preferences.
All you have to do is, simply choose a movie that you enjoy and we will immediately suggest a collection of films that suit your taste.<br>
![image](https://github.com/kinxyo/RecomSys/assets/90744941/51563498-789d-4b5d-bfb1-7173511f212b)
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
streamlit run app.py
```

## Closing Remarks
Completed this project as part of a college assignment.
<br>
We used Streamlit so that we could focus on machine learning part without worrying about the frontend.
Currently our system is content-based but we're very much inclined to push to a hybrid model (Content-based + Collaborative filtering).
<br>
We are also looking to upgrade to Flask to improve the frotend.
### Team
- Kinjalk 
- [Gitansh](https://github.com/Gitansh-Agarwal)
- [Om](https://github.com/Ashu-Pablo) 
- [Himanshu](https://github.com/xendai66)
