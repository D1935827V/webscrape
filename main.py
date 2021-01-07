
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/stocks/')
def stocks():
    return render_template("stocks.html")

@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/login/')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')