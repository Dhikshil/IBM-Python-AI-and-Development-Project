from flask import Flask

app = Flask(__name__)
@app.route('/')

#def home():
    #return "hello world"

def index():
    return {"message": "hello world"}