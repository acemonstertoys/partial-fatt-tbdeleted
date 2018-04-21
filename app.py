from flask import Flask
import json

app = Flask(__name__)

@app.route("/rfids/active")
def get_active_rfids():
    """ Retrieves a list of active RFIDs.

    :returns: Returns an array with two elements. The first is a status code, 
            the second being another array with each of the 10-digit RFID 
            tags of the active members.
    """
    return ["Hello, AMT!"]

@app.route("/rfid/<int:tagID>/active")
def get_rfid_status(tagID):
    """ Retrieves status of a given RFID id.
    
    :tagID: An RFID id number.
    :returns: True or False
    """
    return false

@app.route("/rfid/<int:tagID>/certs")
def get_user_certs(tagID):
    """ Retrieves member status and all certifications associated with a given tagID.

    :tagID: An RFID id number.
    :returns: JSON response with member status, name, and a list of authorizations
    """
    return ["helicopter"]

@app.route("/rfids/authorization", methods=['GET'])
def get_all_certs():
    """ GET method: retrieves all available authorizations 
    
    :returns: dict
    """
    return {"certifications": {"user":["Hello, AMT!"]}}

@app.route("/rfids/authorization", methods=['POST'])
def add_cert():
    """ POST method: Adds a certification for a user.

    :tagID: user's RFID id number
    :authorization: id of the certification this user is being granted
    :value: JSON object with any device-specific metadata
    """
    tagID = request.values['tagID']
    return

@app.route("/")
def index():
    """ / """
    return "Hello, AMT!"

if __name__ == '__main__':
    with open("config.json") as f:
        config = json.load(f)
    app.run(host='0.0.0.0', port=int(config['app']['port']), debug=True)

