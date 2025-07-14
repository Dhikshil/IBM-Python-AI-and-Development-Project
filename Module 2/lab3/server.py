from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = "John"
    return render_template("home.html", name = name)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def about():
    return render_template('contact.html')

@app.route('/users/<username>')
def user_profile(username):
    return render_template('profile.html',  username = username)
