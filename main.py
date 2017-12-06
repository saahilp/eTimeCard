from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import myForms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MAH_SECRET'
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():

    form = myForms.LoginForm()    
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
