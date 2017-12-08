from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy  import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import myForms
import os
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MAH_SECRET'

#file_path = os.path.abspath(os.getcwd())+"/testdatabase.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#add = 'mysql://root:secret@localhost/testdatabase'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(36), unique=True)
    password = db.Column(db.String(256))

class Timestamps(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime)
    timeWorked = db.Column(db.String(10))
    description = db.Column(db.Float)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = myForms.LoginForm()


    if form.validate_on_submit():
        print("12345678992000kvbksbvbja")
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            #if check_password_hash(user.password, form.password.data):
            if(user.password == form.password.data):
                #login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = myForms.RegisterForm()

    if form.validate_on_submit():
        #hashed_password = generate_password_hash(form.password.data, method='sha256')

        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        temp = User.query.all()
        for i in temp:
            print(i.username)
        return '<h1>New user ha been created!</h1>'

    return render_template('registration.html', form=form)

@app.route('/dashboard',  methods=['GET', 'POST'])
def dashboard():

    form = myForms.descriptionForm()

    temp = User.query.all()
    return render_template('dashboard.html', inp = temp, form=form)

@app.route('/start', methods=['GET', 'POST'])
def start():

    form = myForms.descriptionForm()

    if(form.validate_on_submit):

        new_entry = Timestamps(username = form.username.data, startTime = datetime.now(), description = form.description.data)
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return redirect(url_for('start'))

@app.route('/end', methods=['GET', 'POST'])
def end():

    form = myForms.descriptionForm()
    d.hour + d.minute / 60. + d.second / 3600
    old_entry = Timestamps.query.filter_by(username = form.username.data, endTime = None).first()
    old_entry.endTime = datetime.now()

    entr1 = old_entry.startTime.hour +  old_entry.startTime.minute / 60 +  old_entry.startTime.second / 3600
    entr2 = old_entry.endTime.hour + old_entry.endTime.minute / 60 + old_entry.endTime.second / 3600

    diff = entr2 - entr1
    old_entry.timeWorked = float(diff)
    db.session.commit()

    return redirect(url_for('logout'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
