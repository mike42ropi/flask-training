from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")
@app.route("/mikeropi")

def index1():
    return "its ropi"
@app.route("/mike1ropi")

def index2():
    return "Hello world"

@app.route("/bootstrap")

def index4():
    return render_template("bootstrap.html")
app.run()
