@app.route("/rfid/<int:tagID>/certs")
def get_user_certs(tagID):
    """ Retrieves member status and all certifications associated with a given tagID.

    :tagID: An RFID id number.
    :returns: JSON response with member status, name, and a list of authorizations
    """
    certs = []
    certs.append("helicopter training")
    return json.dumps(certs)

@app.route("/rfids/authorization", methods=['GET'])
def get_all_certs():
    """ GET method: retrieves all available authorizations

    :returns: dict
    """
    return json.dumps({"certifications": {"user":["Hello, AMT!"]}})

@app.route("/rfids/authorization", methods=['POST'])
def add_cert():
    """ POST method: Adds a certification for a user.

    :tagID: user's RFID id number
    :authorization: id of the certification this user is being granted
    :value: JSON object with any device-specific metadata
    """
    tagID = request.values['tagID']
    return
