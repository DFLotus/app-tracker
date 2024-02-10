from flask import Blueprint, jsonify
import json

helloWorld = Blueprint("helloWorld", __name__)

@helloWorld.route("/hello", methods=["GET"])
def hello() -> json:
    return jsonify({"message": "Hello World!"})
