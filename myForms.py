from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email')])
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=20)])
