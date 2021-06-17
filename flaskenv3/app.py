from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome<h1>'

@app.route('/hello')
def hello_world():
    return "<h1>Hello World !!!</h1>"


# set FLASK_APP = helloworld.py