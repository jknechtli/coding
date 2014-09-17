# all the imports
import sqlite3
from contextlib import closing	
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash

from forms import LoginForm
	
#configuration
DATABASE = 'db/flaskr.db'
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'password'

#create our little application
app = Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTNGS', silent=True)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()
	
@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

@app.route('/')		
def show_entries():
	cur = g.db.execute('select title, text from entries order by id desc')
	entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	g.db.execute('insert into entries(title,text) values (?, ?)',
		[request.form['title'], request.form['text']])
	g.db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data		
		
		if username == app.config['USERNAME'] and password == app.config['PASSWORD']:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
		else:
			form.errors['username'] = ['Incorrect username or password']
			form.errors['password'] = ['Incorrect username or password']
	
	return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

@app.route('/hqdefault.jgp')
def image():
	
	return redirect(image_for("show_entries"))
	
@app.route("/Counter")
def counter():
	return render_template('Counter.html')

	
if __name__ == '__main__':
	app.run(host="10.0.0.18", port=int("80"))#school="10.222.186.196", home="192.168.0.10", tafe="172.31.31.95", work xp="10.0.0.12