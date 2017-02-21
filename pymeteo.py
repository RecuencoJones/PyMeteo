"""
Module with handlers for Aemet information
"""

import urllib2
import xmltodict

def get_municipality_name(municipality_id):
    """
        Return name of a municipality.

        Parameters
        ----------
        municipality_id : int
            A municipality id.
    """

    url = "http://www.aemet.es/xml/municipios/localidad_%d.xml" % municipality_id

    xml = urllib2.urlopen(url)
    data = xml.read()
    xml.close()

    data = xmltodict.parse(data)

    return data["root"]["nombre"]
