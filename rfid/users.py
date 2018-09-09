import json
import requests

@app.route("/rfids/active")
def get_active_rfids():
    """ Retrieves a list of active RFIDs.

    :returns: Returns an array with two elements. The first is a status code,
            the second being another array with each of the 10-digit RFID
            tags of the active members.
    """
    rp = None
    status = "BAD"
    url = 'https://www.acemonstertoys.org/wp-json/amt/v1/rfids/active'
    headers = {'X-Amt-Auth': get_secret()}
    r = requests.get(url, headers=headers)
    json = r.json()
    rfids = json[1]
    data['rfids'] = r
    rp = ApiResult(rfids, 200)

    return rp

@app.route("/rfid/<int:tagID>/active")
def get_rfid_status(tagID):
    """ Retrieves status of a given RFID id.

    :tagID: An RFID id number.
    :returns: True or False
    """
    return json.dumps(False)

def get_secret():
    file = open('../config.json', 'r')
    data = json.load(file)
    file.close()
    return data['wp-api-secret']

