from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def index():
    return jsonify({"type": "pong"})