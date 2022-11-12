#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application
"""

from flask import Flask, escape

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
