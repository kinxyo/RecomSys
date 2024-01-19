# IMPORTS
import random
from flask import Flask, render_template, request, redirect, url_for
from backend.functions import recommend
from backend.models import db
from backend.models import Records

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

    # DEFAULT BEHAVIOUR (FETCH SEARCH HISTORY)
    movies_searched = []

    search_history = Records.query.order_by(Records.id.desc()).limit(5).all()
        
    for record in search_history:
        id = record.id
        movie, poster = recommend(record.title)
        movies_searched.append({'name': movie[0], 'thumbnail': poster[0], 'id': id})

    if request.method == 'GET':        
        return render_template("index.html", history=movies_searched)

    
    elif request.method == 'POST':
        
        recommendations = []

        # GETTING RECOMMENDATION
        film = request.form['film']
        movie, poster = recommend(film)
        suggested = random.randint(0,4)

        print("suggestion index ->", suggested)
        
        # ADDING TO RECORDS 
        if movie and poster:
            db.session.add(Records(title=film, recom_mov=movie[suggested], recom_thum=poster[suggested]))
        else:
            print("Lists are empty")
        db.session.commit()
        
        for i in range(0,5):
            recommendations.append({'title': movie[i], 'poster': poster[i]})

        return render_template("index.html", recommendations=recommendations, history=movies_searched)
    

@app.route('/delete/<int:mid>')
def clear_records(mid):
    record = Records.query.filter_by(id=mid).first()
    try:
        db.session.delete(record)
        db.session.commit()
    except:
        pass
    
    return redirect(url_for('Home'))
        


if __name__ == "__main__":
    app.run(debug=True)