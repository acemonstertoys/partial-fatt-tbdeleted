from flask import Flask, request
import json
from response import *


def create_app(config=None):
    app = Flask(__name__) 
    app.config.update(config or {})
    register_blueprints(app) # store all app code in blueprints.
    register_other_things(app)
    return app

class FATTApi(object):
    def __init__(self, config):
        self.flask_app = create_app(config)
        self.flask_app.FATTApiContext = self
    def __call__(self, environ, start_response):
        return self.flask_app(environ, start_response)
        # app.run(host='0.0.0.0', port=int(config['app']['port']), debug=True)

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

@app.route("/")
def index():
    """ / """
    return "Hello, AMT!"

if __name__ == '__main__':
    app_instance = FATTApi()
