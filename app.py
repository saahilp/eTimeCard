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
    timeWorked = db.Column(db.Float)
    description = db.Column(db.String(50))
    date = db.Column(db.DateTime)

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
        print("1234567899200kvbksbvbja")
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
        return '<h1>New user has been created!</h1>'

    return render_template('registration.html', form=form)

@app.route('/dashboard',  methods=['GET', 'POST'])
def dashboard():

    form = myForms.descriptionForm()
    print(form.username.data)
    print(form.timeWorked.data)
    if form.validate_on_submit():
        print(form.username.data)
        print(form.timeWorked.data)
        new_timeStamp = Timestamps(username = form.username.data, timeWorked = form.timeWorked.data, date = form.date.data, description = form.description.data)
        db.session.add(new_timeStamp)
        db.session.commit()

        temp = Timestamps.query.all()
        for i in temp:
            print(i.username)
            print(i.hours)
        return render_template('showTables.html', inp = temp)

    #temp = Timestamps.query.filter_by(username = new_timeStamp.username).all()

    return render_template('dashboard.html', form = form)


@app.route('/showTables')
def showTables():

    temp = Timestamps.query.all()

    return render_template('showTables.html', inp = temp)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



if __name__ == '__main__':
    # Bind to PORT if defied, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
