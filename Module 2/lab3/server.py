from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = "John"
    return render_template("home.html", name = name)

@app.route('/about')
def about():
    return render_template("about.html")