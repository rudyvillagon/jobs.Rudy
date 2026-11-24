from flask import Blueprint, request, jsonify
from fruit_management import FruitManagement
from connect_db import MakeConectionDb
from permissions import role_required

fruit_routes = Blueprint("fruits", __name__)

@fruit_routes.route("/fruits", methods=["GET"])
@role_required("Administrator", "User")
def get_all_fruits():

    db = MakeConectionDb()

    try:
        all_fruits = FruitManagement(db)

        result = all_fruits.select_all_fruit()

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(result), 200

    finally:
        db.close()

@fruit_routes.route("/fruits/<int:fruit_id>", methods=["GET"])
@role_required("Administrator", "User")
def get_one_specify_fruit(fruit_id):

    db = MakeConectionDb()

    try:
        specify_fruit = FruitManagement(db)

        result = specify_fruit.select_fruit(fruit_id)

        if result == "fruit_not_found":
            return jsonify(error= result), 404

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500


        return jsonify(result), 200

    finally:
        db.close()

@fruit_routes.route("/fruits/<int:fruit_id>", methods= ["DELETE"])
@role_required("Administrator")
def delete_fruit(fruit_id):

    db = MakeConectionDb()

    try:
        del_inf = FruitManagement(db)

        result = del_inf.dele_fruit(fruit_id)

        if result == "fruit_not_found":
            return jsonify(error= result), 404
        
        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(massage= result), 200

    finally:
        db.close()

@fruit_routes.route("/fruits/<int:fruit_id>", methods= ["PATCH"])
@role_required("Administrator")
def modify_fruit(fruit_id):

    db = MakeConectionDb()

    try:
        mod_fruit = FruitManagement(db)

        result = mod_fruit.modify_fruit(fruit_id)

        if result == "fruit_not_found":
            return jsonify(error= result), 404

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(message = result), 200

    finally:
        db.close()

@fruit_routes.route("/fruits", methods= ["POST"])
@role_required("Administrator")
def create_fruit():
    body_request = request.json

    db = MakeConectionDb()

    try:

        manage = FruitManagement(db)

        result = manage.create_new_fruit(body_request)

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(massage = result), 200 

    finally:
        db.close()

