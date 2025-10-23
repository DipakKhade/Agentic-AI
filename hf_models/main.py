from flask import Flask

app = Flask(__name__)

@app.get('/')
def default():
    return {'message':'server is up'}