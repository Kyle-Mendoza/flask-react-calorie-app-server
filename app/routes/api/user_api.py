from flask import Blueprint, jsonify

user_api = Blueprint("user_api", __name__)


@user_api.route("/test")
def test():
  return jsonify(
    {
      "message": "This is on user_api route test"
    }
  )

@user_api.route("/get_user")
def get_user():
  pass
