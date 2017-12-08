from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import myForms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MAH_SECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C://Users//admin//eTimeCard//testdatabase.db'
db = SQLAlchemy(app)
Bootstrap(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = myForms.LoginForm()
    return render_template('login.html', form=form)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = myForms.RegisterForm()

    return render_template('registration.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=33507)
