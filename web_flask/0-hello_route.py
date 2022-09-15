#!/usr/bin/python3
"""starts a flask web app listenning on port 5000"""

from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hell0():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
