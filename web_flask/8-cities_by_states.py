#!/usr/bin/python3
"""starts a flask web app listening on port 5000"""

from flask import Flask, render_template
from models import storage, State
import os

app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def close_session(exception=None):
    """closes the sqlalchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def show_cities_by_state():
    """retrieve States from storage and show in html page"""
    return render_template(
        "8-cities_by_states.html",
        dict_states=storage.all(State)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
