from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Length

class LoginForm(Form):
	username = TextField('Username', validators = [InputRequired(), Length(min=5, max=32)])
	password = PasswordField('Password', validators = [InputRequired(), Length(min=8, max=32)])

#class PostForm(Form):
	#text feild name 	
	#string feild text