#!/usr/bin/python3
"""starts a flask web app listenning on port 5000"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def close_session(exception=None):
    """closes the sqlalchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def show_states():
    """retrieve States from storage and show in html page"""
    return render_template(
        "7-states_list.html",
        dict_states=storage.all(State)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
