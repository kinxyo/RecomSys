# IMPORTS
import random
from flask import Flask, render_template, request
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


    if request.method == 'POST':
        
        # GETTING RECOMMENDATION
        film = request.form['film']
        movie, poster = recommend(film)
        suggested = random.randint(0,5)
        
        # ADDING TO RECORDS 
        db.session.add(Records(title=film, recom_mov=movie[suggested], recom_thum=poster[suggested])) #the error is probably because there are no records yet, "what about the exception msg?" yeah it's bullshit. people who use python aren't really good at coding you know.
        db.session.commit()
        
        return render_template("index.html", posters=poster)
    

    elif request.method == 'GET':
        movies_searched = []

        search_history = Records.query.order_by(Records.sno.desc()).limit(5).all()
        
        for record in search_history:
            movie, poster = recommend(record.title)
            movies_searched.append({'name': movie[0], 'thumbnail': poster[0]})

        return render_template("index.html", history=movies_searched)


if __name__ == "__main__":
    app.run(debug=True)