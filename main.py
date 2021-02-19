from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Doe eens normaal!'

@app.route('/cow')
def cow():
    return 'Boodschaaap!'

