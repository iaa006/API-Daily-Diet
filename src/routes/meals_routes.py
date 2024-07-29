from flask import Blueprint, request, jsonify
from src.models.meal import Meal
meals_blueprint = Blueprint('meals', __name__)

@meals_blueprint.route('/', methods=['POST'])
def create_meal():
    data = request.get_json()
    new_meal = Meal(name=data['name'], description=data['description'], date_time=data['date_time'], on_diet=data['on_diet'])
    new_meal.create_meal()

    return jsonify(new_meal.meal_to_dict()), 201

@meals_blueprint.route('/', methods=['GET'])
def get_meals():
    meals = [Meal.to_dict(meal) for meal in Meal.get_users()]

    return jsonify({'Meals': meals})

@meals_blueprint.route('/<int:id>', methods=['GET'])
def get_meal(id):
    meal = Meal.get_user(id)
    
    return jsonify(Meal.to_dict(meal))

@meals_blueprint.route('/<int:id>', methods=['PUT'])
def update_meal(id):
    data = request.get_json()
    Meal.update_user(id, data)

    return jsonify({'message': 'Meal updated with success'})

@meals_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_meal(id):
    Meal.delete_user(id)

    return jsonify({'message': 'Meal deleted with success'})