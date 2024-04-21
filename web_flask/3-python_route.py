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
    formatted_text = text.repalce('-', ' ')
    return f"c {formatted_text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def costom_text_python(text):
    """return python {formatted text}"""
    formatted_text = text.replace('-', ' ')
    return f"python {formatted_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
