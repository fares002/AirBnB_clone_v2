#!/usr/bin/python3
"""start falsk application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def HelloHBNB():
    """return HelloHBNB"""
    return "HelloHBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
