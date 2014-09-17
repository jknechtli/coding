from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello world"
	
	
if __name__ == '__main__':
	app.run() # turn DEBUG to False and add (host='0.0.0.0')