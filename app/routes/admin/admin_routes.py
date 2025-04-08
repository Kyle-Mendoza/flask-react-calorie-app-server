from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.models.admin import Admin

admin = Blueprint("admin_routes", __name__)

@admin.route("/login", methods=['POST'])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  admin = Admin.query.filter_by(username=username).first()


  if not username and not password:
    return jsonify(
      {
        "message": "Some fields are empty. Please try again!"
      }
    ), 401
  
  if admin and admin.check_password(password):
    token = create_access_token(identity=admin.id)
    return jsonify({
      "access_token": token,
      "admin": {
        "id": admin.id,
        "username": admin.username,
      }
    }), 200
  
  return jsonify({
    "message": "Invalid credentials!"
  }), 401