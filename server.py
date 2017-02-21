from flask import Flask
from urllib2 import HTTPError

import pymeteo

app = Flask(__name__)

@app.route("/api/weather/<int:municipality_id>")
def get_name_of_municipality(municipality_id):
    """
        Retrieves weather for a given municipality id.

        Parameters
        ----------
        municipality_id : int
            Id of the municipality from which to retrieve information.
    """

    try:
        municipality_name = pymeteo.get_municipality_name(municipality_id)

        result = """
            Name: {name}
            Municipality ID: {id}
        """.format(name=municipality_name, id=municipality_id)
    except HTTPError:
        result = "Invalid municipality id: %d" % municipality_id

    return result

if __name__ == "__main__":
    app.run()
