# IMPORTS
import random
from flask import Flask, render_template, request, redirect, url_for
from backend.functions import *
from backend.models import Records, db

# APP CONFIG
app = Flask(__name__, template_folder="pages")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///recomsys.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


# ROUTES
@app.route('/', methods=['GET','POST'])
def Home():
    found = True
    # DEFAULT BEHAVIOUR (FETCH SEARCH HISTORY)
    user_taste = []

    search_history = Records.query.order_by(Records.id.desc()).limit(5).all()
        
    for record in search_history:
        id = record.id
        movie, poster = recommend_from_history(record.movie_searched)
        user_taste.append({'name': movie[0], 'thumbnail': poster[0], 'id': id})

    if request.method == 'GET':        
        return render_template("index.html", history=user_taste, status=found)

    
    elif request.method == 'POST':
        
            film = request.form['film']

            matching_movies = search_movie(film)            
            matching_movies_list = matching_movies.to_dict('records')

            if matching_movies.empty:
                found = False

            for movie in matching_movies_list:
                movie['poster'] = fetch_poster(movie['movie_id'])
            

            return render_template("index.html", searchresults=matching_movies_list, status=found, history=user_taste)

    

@app.route('/delete/<int:mid>')
def clear_records(mid):
    record = Records.query.filter_by(id=mid).first()
    try:
        db.session.delete(record)
        db.session.commit()
    except:
        pass
    
    return redirect(url_for('Home'))

@app.route('/recom/<int:movie_id>')
def recom(movie_id):
    # Fetch the selected movie
    # GETTING RECOMMENDATION

    recommendations = []

    movie, poster, id, movie_searched = recommend(movie_id)
    suggested = random.randint(0,4)
    
    # ADDING TO RECORDS 
    if movie and poster:
        try:
            db.session.add(Records(movie_searched=movie_searched, id_recom=id[suggested], movie_recom=movie[suggested], thumbnail_recom=poster[suggested]))
            db.session.commit()
            print(f"{movie_searched} added to records")
        except:
            print("Already in records")
    else:
        print("Lists are empty, couldn't add to records")
        
    for i in range(0,5):
        recommendations.append({'id': id[i], 'title': movie[i], 'poster': poster[i]})

    return render_template("recom.html", recommendations=recommendations, star=retrieve_movie(movie_id))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)