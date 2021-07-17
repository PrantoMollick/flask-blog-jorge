from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(Form):
    fullname = StringField('Full name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = StringField('New Password', validators=[DataRequired(), 
                            EqualTo('confirm', 
                            message='Password must match'), 
                            Length(min=4, max=80)])
    confirm = PasswordField('Repeat Password')


