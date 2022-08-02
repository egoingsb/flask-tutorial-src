from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Root"

@app.route("/topics")
def topics():
    return "topics"

@app.route("/topics/<id>")
def topicsById(id):
    return "topics/"+id

@app.route("/plus/<int:left>/<int:right>")
def topicsByIdToNum(right, left):
    return str(left+right)

