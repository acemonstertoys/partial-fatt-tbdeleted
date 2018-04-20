from flask import Flask

from ConfigParser import SafeConfigParser

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, AMT!"

if __name__ == '__main__':
    app.run(port=80, debug=True)
