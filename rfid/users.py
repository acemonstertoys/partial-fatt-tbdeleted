
@app.route("/rfids/active")
def get_active_rfids():
    """ Retrieves a list of active RFIDs.

    :returns: Returns an array with two elements. The first is a status code,
            the second being another array with each of the 10-digit RFID
            tags of the active members.
    """
    rp=None
    status="BAD"
    if status is "OK":
        rfids = []
        data['rfids'] = r
        rp=ApiResult(rfids, 200)
    else:
        raise ApiException('Oh no its bad')
    return rp
#    return json.dumps([status, data])

@app.route("/rfid/<int:tagID>/active")
def get_rfid_status(tagID):
    """ Retrieves status of a given RFID id.

    :tagID: An RFID id number.
    :returns: True or False
    """
    return json.dumps(False)

