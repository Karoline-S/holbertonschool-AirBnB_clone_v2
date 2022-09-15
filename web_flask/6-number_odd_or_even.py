#!/usr/bin/python3
"""starts a flask web app listenning on port 5000"""

from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")


@app.route("/", strict_slashes=False)
def hello():
    """returns a greeting when route is queried"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb for /hbnb query"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """displays url text on page"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """displays url text on page with default set"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_check(n):
    """displays url text on page with default set"""
    return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def rendering(n):
    """displays a template if n is an int"""
    return render_template(
        "5-number.html",
        insert="Number: {}".format(n)
    )


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """displays dynamic variable in rendered template"""
    if n % 2 == 0:
        state = "even"
    else:
        state = "odd"
    return render_template(
        "6-number_odd_or_even.html",
        insert="Number: {} is {}".format(n, state)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
