from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms import Form, BooleanField, TextField, PasswordField, validators

class LoginForm(Form):
	username = TextField('Username', validators = [InputRequired(), Length(min=5, max=32)])
	password = PasswordField('Password', validators = [InputRequired(), Length(min=8, max=32)])

#class PostForm(Form):
	#text feild name 	
	#string feild text
	
class RegistrationForm(Form):
	username = TextField('Username', [InputRequired(), Length(min=4, max=25)])
	password = PasswordField('New Password', [
		InputRequired(),
		EqualTo('confirm', message='Passwords must match')
	])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept the TOS', [InputRequired()])