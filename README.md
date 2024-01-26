# CinemaScope
![Frame 12](https://github.com/kinxyo/RecomSys/assets/90744941/979e90f7-2387-4708-ae06-cb3390e90a1c)

# POSTERINTRO
![recomsys-readme_poster](https://github.com/kinxyo/RecomSys/assets/90744941/30381925-9b0a-4325-847e-8af255789fe6)
## How To Use

### Setup
#### Clone Repository
```
https://github.com/kinxyo/RecomSys.git
```
#### Enter Virtual Env 
```
py -3 -m venv cinema
```
```
source cinema/scripts/activate
```
#### Install Requirements
```
pip install -r requirements.txt
```
#### Generate Artifacts (Output Model)
```
python ml.py
```

### Run
```
python wsgi.py
```
![recom_sissy_demo](https://github.com/kinxyo/RecomSys/assets/90744941/8b0ce292-c0e4-4c7b-8fca-c4d0ae969cbe)
## Closing Remarks
Done as part of a college project.
<br>
<br>
We have also put the jupyter notebook in it for easy modification of tags for recommendation system.
To convert it into python script:
```
jupyter nbconvert --to script YourNotebook.ipynb
```
You can learn more about **Cosine Similarity** [here](https://www.learndatasci.com/glossary/cosine-similarity/).
<br>
Find **Dataset** [here](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv).
