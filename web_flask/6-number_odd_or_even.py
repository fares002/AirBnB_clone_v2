#!/usr/bin/python3
"""start flask application"""
from flask import Flask, render_template
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
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}".format(formatted_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def custom_text_python(text="is cool"):
    """return python {formatted text}"""
    formatted_text = text.replace('_', ' ')
    return "python {}".format(formatted_text)


@app.route('/number/<n>', strict_slashes=False)
def imnumber(n):
    """return only numbers"""
    return "{:d} is number".format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """return html page with the n variable"""
    return render_template("5-number.html", test=f"Number: {n}")


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """return odd or even"""
    if n % 2 == 0:
        msg = f"{n} is even"
        return render_template("6-number_odd_or_even.html", test=msg)
    else:
        return render_template("6-number_odd_or_even.html", test=f"{n} is odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
