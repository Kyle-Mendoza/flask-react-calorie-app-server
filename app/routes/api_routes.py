from flask import Blueprint, jsonify

api = Blueprint("api_routes", __name__)

@api.route("/get_message")
def get_message():
  data = {
    "message": "Flask Cors Connected Successfully!"
  }

  return jsonify(data)
