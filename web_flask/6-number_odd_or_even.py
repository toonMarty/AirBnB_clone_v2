#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application
"""

from flask import Flask, escape, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
    This function will return the string, Hello HBNB!
    Returns:
        str: a string
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    This function will return the string, HBNB!
    Returns:
        str: a string, HBNB
    """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """
    This function will return the string, c followed by some text
    Returns:
        str: a string, c <text>
    """
    return "C %s" % escape(' '.join(text.split('_')))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """
    This function will return the string, python followed by some text
    Returns:
        str: a string, python <text>
    """
    return "Python %s" % escape(' '.join(text.split('_')))


@app.route('/number/<int:n>')
def number(n):
    """
    This function will display “n is a number” only if n is an
    integer
    Args:
        n: int
    Returns:
        int: a number, n
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    This function will display “n is a number” only if n is an
    integer using a template
    Args:
        n: int
    Returns:
        int: a number, n
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<n>')
def number_odd_or_even(n):
    """
    This function will display a HTML page only if n is an integer
    Args:
        n: int
    Returns:
        int: a number, n
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
