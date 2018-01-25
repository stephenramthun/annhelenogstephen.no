from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    passkey = StringField('passkey', validators = [InputRequired()])

class AnswerForm(FlaskForm):
    answer = RadioField('answer', choices = [], validators = [InputRequired()])

class RegisterForm(FlaskForm):
    first_name = StringField('first_name', validators = [InputRequired()])
    last_name = StringField('last_name', validators = [InputRequired()])
    allergies = StringField('allergies')
    vegan = BooleanField('vegan')
    vegetarian = BooleanField('vegetarian')
    kids_menu = BooleanField('kids_menu')
