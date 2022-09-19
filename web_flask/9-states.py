#!/usr/bin/python3
"""starts a flask web app listening on port 5000"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def close_session(exception=None):
    """closes the sqlalchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def show_states(id=None):
    """retrieve States from storage and show in html page"""

    dict_states = storage.all(State)

    if id is None:
        return render_template(
            "9-states.html",
            dict_states=dict_states
        )
    else:
        state_id = 'State.' + id
        return render_template(
            "9-states.html",
            dict_states=dict_states,
            state_id=state_id
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
