from flask import Blueprint

admin = Blueprint("admin_routes", __name__)

@admin.route("/login")
def login():
  pass
