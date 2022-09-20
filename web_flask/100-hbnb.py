#!/usr/bin/python3
"""starts a flask web app listening on port 5000"""

from flask import Flask, render_template
from models import storage, State, Amenity, Place

app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def close_session(exception=None):
    """closes the sqlalchemy session"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def show_hbnb():
    """retrieves all data for hbnb page display"""
    return render_template(
        "100-hbnb.html",
        dict_states=storage.all(State),
        dict_amenities=storage.all(Amenity),
        dict_places=storage.all(Place)
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
