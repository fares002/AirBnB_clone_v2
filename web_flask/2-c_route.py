#!/usr/bin/python3
"""start flask application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def custom_text(text):
    """return c {formatted text}"""
    formatted_text = text.replace("_", " ")
    return "C {}".format(formatted_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
