from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/read/<id>")
def read(id):
    return render_template("read.html")

