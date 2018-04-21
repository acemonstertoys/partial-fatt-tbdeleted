from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, AMT!"

if __name__ == '__main__':
    with open("config.json") as f:
        config = json.load(f)
    app.run(host='0.0.0.0', port=int(config['app']['port']), debug=True)
