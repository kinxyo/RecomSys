from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

db = SQLAlchemy()

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=50)], render_kw={'placeholder': 'Password'})
    submit = SubmitField("Submit")

class SignUpForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=50)], render_kw={'placeholder': 'Password'})
    submit = SubmitField("Submit")



class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False) # film_searched
    recom_mov = db.Column(db.String(500), nullable=False)
    recom_thum = db.Column(db.String(800), nullable=False)
    date_searched = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repre__(self) -> str:
        return f"{self.sno}. {self.title}"

# recom = recommended   