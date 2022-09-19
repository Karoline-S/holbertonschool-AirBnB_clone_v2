#!/usr/bin/python3
"""starts a flask web app listening on port 5000"""

from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def close_session(exception=None):
    """closes the sqlalchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def show_states_cities_amenities():
    """retrieve States from storage and show in html page"""

    return render_template(
        "10-hbnb_filters.html",
        dict_states=storage.all(State),
        dict_amenities=storage.all(Amenity)
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
