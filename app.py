# IMPORTS
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from backend.functions import *

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repre__(self) -> str:
        return f"{self.sno}-> {self.title}"
    

@app.route('/', methods=['GET','POST'])
def Home():
    # todo = Todo(title="Listen Close!", desc="Start investing in Stocks!")
    # db.session.add(todo)
    # db.session.commit(todo)
    if request.method == 'POST':
        film = request.form['film']
        movie, poster = recommend(film)
        for i in range(0,5):
            print(movie[i])
        return render_template("index.html", posters=poster)
    elif request.method == 'GET':
        movies_searched = []
        search_history = []
        with open("history.txt","r") as search_records:
            history = search_records.readlines()
            for movies in history:
                tmp_list = movies.split("\n")
                search_history.insert(0, tmp_list[0])            
            
            for i in range(5):
                movie, poster = recommend(search_history[i])
                movies_searched.append({'name': movie[i], 'thumbnail': poster[i]})

        print(movies_searched)
        return render_template("index.html", history=movies_searched)

if __name__ == "__main__":
    app.run(debug=True)


""" 
     with open("history.txt","r") as check:
            content = check.read()
            if film in content:
                print("film already present in records")
                pass
            else:
                print(f"adding {film}")
                with open('history.txt','a') as file:
                    file.write(f"{film}\n")
"""
