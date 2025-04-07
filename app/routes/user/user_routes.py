from flask import Blueprint

main = Blueprint('main_routes', __name__)

@main.route("/login")
def login():
  pass

@main.route("/register")
def register():
  pass
