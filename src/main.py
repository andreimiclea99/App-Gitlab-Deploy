# Imagine a real application here with database, caching etc... 
# this is just a placeholder

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/status")
def health():
    return
