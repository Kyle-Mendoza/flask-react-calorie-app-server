from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.extensions import db 
from app.models.food import Food 


food = Blueprint("food_routes", __name__)

@food.before_request
@jwt_required()
def require_jwt():
    pass

@food.route("/")
def get_all_food():
    foods = Food.query.all()

    food_list = [
        {
            "id": food.id,
            "name": food.name,
            "calories": food.calories,
            "carbs": food.carbs,
            "protein": food.protein,
            "fat": food.fat,
            "serving_size": food.serving_size
        }
        for food in foods
    ]

    return jsonify(food_list)

@food.route("/new", methods=['POST'])
def create_food():
    data = request.json 

    if not all(key in data for key in ["name", "calories", "carbs", "protein", "fat", "serving_size"]):
        return jsonify({
            "message": f"missing required fields!"
        }), 400
    
    new_food = Food(
        name=data["name"],
        calories=data["calories"],
        carbs=data["carbs"],
        protein=data["protein"],
        fat=data["fat"],
        serving_size=data["serving_size"]
    )

    db.session.add(new_food)
    db.session.commit()

    return jsonify({
        "message": f"{new_food.name} has been added!",
        "food": {
            "name": new_food.name,
            "calories": new_food.calories,
            "carbs": new_food.carbs,
            "protein": new_food.protein,
            "fat": new_food.fat,
            "serving_size": new_food.serving_size
        }
    }), 200

@food.route("/<int:id>")
def select_food(id):
    food = Food.query.get_or_404(id)

    food_info = [
        {
            "id": food.id,
            "name": food.name,
            "calories": food.calories,
            "carbs": food.carbs,
            "protein": food.protein,
            "fat": food.fat,
            "serving_size": food.serving_size
        }
    ]

    return jsonify(food_info)

@food.route("/<int:id>/edit", methods=['POST'])
def edit_food(id):
    food = Food.query.get_or_404(id)
    data = request.json

    if not food:
        return jsonify({
            "message": "item does not exists!"
        }), 404

    food.name = data.get("name", food.name)
    food.calories = data.get("calories", food.calories)
    food.carbs = data.get("carbs", food.carbs)
    food.protein = data.get("protein", food.protein)
    food.fat = data.get("fat", food.fat)
    food.serving_size = data.get("serving_size", food.serving_size)

    db.session.commit()

    return jsonify({
        "message": f"{food.name} nutritional fact has been updated!",
        "food": {
            "id": food.id,
            "name": food.name,
            "calories": food.calories,
            "carbs": food.carbs,
            "protein": food.protein,
            "fat": food.fat,
            "serving_size": food.serving_size
        }
    }), 200

@food.route("/<int:id>/delete", methods=['DELETE'])
def delete_food(id):
    food = Food.query.get_or_404(id)
    food_name = food.name

    db.session.delete(food)
    db.session.commit()

    return jsonify({
        "message": f"{food_name} has been removed!"
    }), 200