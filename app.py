# IMPORTS
import random
from flask import Flask, render_template, request, redirect, url_for
from backend.functions import recommend
from backend.models import LoginForm, SignUpForm, Users, db
from backend.models import Records
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt


# APP CONFIG
app = Flask(__name__, template_folder="pages")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///recomsys.db"
app.config['SECRET_KEY'] = 'thisissecretkey '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
hashit = Bcrypt(app)
supervisor = LoginManager(app)
supervisor.init_app(app)
supervisor.login_view = 'login'

with app.app_context():
    db.create_all()

@supervisor.user_loader
def load_user(id):
    return Records.query.get(int(id))

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
        
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and hashit.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template('dashboard.html', form=form)

@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = hashit.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('signup.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)