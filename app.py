# IMPORTS
import random
from flask import Flask, render_template, request, redirect, url_for
from backend.functions import fetch_poster, search_movie_by_name, get_recommendations, get_all
from backend.models import Records, db

# APP CONFIG
app = Flask(__name__, template_folder="pages")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///recomsys.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DATABASE
db.init_app(app)
with app.app_context():
    db.create_all()

# ROUTES
@app.route('/', methods=['GET','POST'])
def Home():
    # DEFAULT BEHAVIOUR (FETCH SEARCH HISTORY)
    search_found = True    

    # Extractive Saved Recommendations
    search_history = Records.query.order_by(Records.id.desc()).limit(5).all()
    user_taste = []    
    for record in search_history:
        id = record.id
        title = record.recom_mov
        poster = record.recom_thumb
        user_taste.append({'name': title, 'thumbnail': poster, 'id': id})


    # GET REQUEST
    if request.method == 'GET':        
        return render_template("index.html", history=user_taste, search_found=search_found)

    
    # POST REQUEST
    elif request.method == 'POST':
        
            # Getting the searched term
            film = request.form['film']

            # Search Results
            matching_movies = search_movie_by_name(film)
            matching_movies_list = matching_movies.to_dict('records')

            # If no results found
            if matching_movies.empty:
                search_found = False
            else:
                # Fetching posters
                for movie in matching_movies_list:
                    movie['poster'] = fetch_poster(movie['movie_id'])
            return render_template("index.html", searchresults=matching_movies_list, search_found=search_found, history=user_taste)
    else:
        return render_template("404.html")
    

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

    # Getting recommendations
    recommendation = get_recommendations(movie_id)
    if recommendation is None:
        return render_template("404.html")
    else:
        movie, poster, id = recommendation

    random_number = random.randint(0,4)
    
    # Adding Recommendation to Database
    if movie and poster:
        try:
            db.session.add(Records(movie_searched_id=movie_id, recom_mov=movie[random_number], recom_thumb=poster[random_number]))
            db.session.commit()
            print(f"Added {movie[random_number]} #{movie_id} to records")
        except Exception as e:
            if e:
                print(f"Error adding {movie[random_number]} to records: {e}")
            else:
                print("Already in records")
    else:
        print("Lists are empty, couldn't add to records")
        
    # Creating a dictionary for frontend to render recommendations
    recommendations = []
    for i in range(0,5):
        recommendations.append({'id': id[i], 'title': movie[i], 'poster': poster[i]})

    return render_template("recom.html", recommendations=recommendations, star=get_all(movie_id))

# ERROR ROUTE
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404