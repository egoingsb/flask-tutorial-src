from flask import Flask, render_template

app = Flask(__name__)

topics = [
    {'id':1, 'title':'html', 'body':'html is ...'},
    {'id':2, 'title':'css', 'body':'css is ...'},
    {'id':3, 'title':'js', 'body':'js is ...'}
]

@app.route("/")
def index():
    return render_template("welcome.html", topics=topics)

@app.route("/read/<int:id>")
def read(id):
    topic = None
    for row in topics:
        if row['id'] == id:
            topic = row
            break
    return render_template("read.html", topics=topics, topic=topic)

