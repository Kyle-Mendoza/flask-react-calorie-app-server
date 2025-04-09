from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.models.user import User
from app.extensions import db 

main = Blueprint('main_routes', __name__)


@main.route("/login", methods=["POST"])
def login():
  data = request.json 
  username = data.get("username")
  password = data.get("password")

  user = User.query.filter_by(username=username).first()

  if not username and not password:
    return jsonify({
      "message": "please fill up all fields!"
    }), 401
  
  if user and user.check_password(password):
    access_token = create_access_token(identity="user.id")

    return jsonify({
      "message": "login successfully!",
      "token": access_token,
      "user": {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "weight": user.weight,
        "height": user.height,
        "physical_activity_level": user.physical_activity_level,
        "birthdate": user.birthdate,
      }
    }), 200

  return jsonify({
    "message": "wrong password, please try again"
  })

@main.route("/register", methods=["POST"])
def register():
  data = request.json 
  email = data["email"]
  username = data["username"]
  first_name = data["firstname"]
  last_name = data["lastname"]
  weight = data["weight"]
  height = data["height"]
  physical_activity_level = data["physical_activity_level"]
  birthdate = data["birthdate"]
  password = data["password"]

  field_list = ["email", "username", "firstname", "lastname", "weight", "height", "physical_activity_level", "birthdate", "password"]

  if not all(key in data for key in field_list):
    return jsonify({
      "message": "some fields are missing, please fill all fields!"
    }), 401 
  
  new_user = User(
    email=email, 
    username=username,
    first_name=first_name, 
    last_name=last_name, 
    weight=weight, 
    height=height, 
    physical_activity_level=physical_activity_level, 
    birthdate=birthdate)
  new_user.set_password(password)


  db.session.add(new_user)
  db.session.commit()

  return jsonify({
    "message": f"Account {username} has been created!"
  }), 200