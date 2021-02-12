from flask import Flask


app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Doe eens normaaaaaaaaal!'

@app.route('/cow')
def cow():
    return 'Boodschaaaaaap!'

