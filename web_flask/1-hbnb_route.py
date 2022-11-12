#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
