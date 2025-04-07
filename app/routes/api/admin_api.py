from flask import Blueprint, jsonify

admin_api = Blueprint('admin_api',__name__)

@admin_api.route("/test")
def test():
  return jsonify({
    "message": "This is an admin api"
  })
