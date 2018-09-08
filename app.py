from flask import Flask, request
import json
import sys
from response import *


app = Flask(__name__) 



@app.route("/")
def index():
    """ / """
    return "Hello, AMT!"

if __name__ == '__main__':
    config = {'app': {'port': 80}} # sys.argv
    if len(sys.argv)>1:
        config['app']['port'] = sys.argv[1]
    app.run(host='0.0.0.0', port=int(config['app']['port']), debug=True)
    
    # app.config.update(config or {})
