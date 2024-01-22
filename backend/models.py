from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_searched = db.Column(db.String(500), nullable=False, unique=True) # film_searched
    id_recom = db.Column(db.Integer, nullable=False)
    movie_recom = db.Column(db.String(500), nullable=False)
    thumbnail_recom = db.Column(db.String(800), nullable=False)
    date_searched = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repre__(self) -> str:
        return f"{self.sno}. {self.title}"

# recom = recommended   