from flask import Blueprint 

food = Blueprint("food_routes", __name__)

@food.route("/")
def get_food():
    pass