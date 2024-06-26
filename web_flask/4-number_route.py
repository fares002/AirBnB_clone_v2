#!/usr/bin/python3
"""start flask application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def custom_text_c(text):
    """return c {formatted}"""
    formatted_text = text.repalce('_', ' ')
    return "C {}".format(formatted_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def custom_text_python(text="is cool"):
    """return python {formatted text}"""
    formatted_text = text.replace('_', ' ')
    return "python {}".format(formatted_text)


@app.route('/number/<int:n>', strict_slashes=False)
def imnumber(n):
    """return only numbers"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
