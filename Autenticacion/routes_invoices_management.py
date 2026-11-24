from flask import Blueprint, request, jsonify, g
from invoices_management import InvoicesManagement
from connect_db import MakeConectionDb
from permissions import role_required
from fruit_management import FruitManagement
from datetime import date

invoices_routes = Blueprint("invoices", __name__)

@invoices_routes.route("/invoices", methods=["GET"])
@role_required("Administrator")
def get_all_invoices():

    db = MakeConectionDb()

    try:
        all_invoices = InvoicesManagement(db)

        result = all_invoices.select_invoices

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(result), 200

    finally:
        db.close()

@invoices_routes.route("/invoices/<int:invioces_id>", methods=["GET"])
@role_required("Administrator", "User")
def get_one_specify_invoices(invioces_id):

    db = MakeConectionDb()

    try:
        specify_invoices = InvoicesManagement(db)

        result = specify_invoices.select_invoices(invioces_id)

        if result == "invoices_not_found":
            return jsonify(error= result), 404

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(result), 200

    finally:
        db.close()

@invoices_routes.route("/invoices/<int:invioces_id>", methods=["DELETE"])
@role_required("Administrator")
def delete_invoices(invoices_id):

    db = MakeConectionDb()

    try:

        del_invoices = InvoicesManagement(db)

        result = del_invoices.dele_invoice(invoices_id)

        if result == "invoices_not_found":
            return jsonify(error= result), 404

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(message= result), 200

    finally:
        db.close()


@invoices_routes.route("/invoices/<int:invioces_id>", methods= ["PATCH"])
@role_required("Administrator")
def modify_invoices(invoices_id):

    db = MakeConectionDb()

    try:
        mod_invoices = InvoicesManagement(db)

        result = mod_invoices.modify_invoice(invoices_id)

        if result == "invoices_not_found":
            return jsonify(error= result), 500

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500 

        return jsonify(message= result), 200

    finally:
        db.close()

@invoices_routes.route("/invoices", methods= ["POST"])
@role_required("Administrator"  )
def create_invoices():

    body_request = request.json

    db = MakeConectionDb()

    try:

        manage = InvoicesManagement()

        result = manage.create_new_invoice(body_request)

        if isinstance(result, str) and result.startswith("Database_error:"):
            return jsonify(error= result), 500

        return jsonify(message= result), 200

    finally:
        db.close()

@invoices_routes.route("/purchase", methods=["POST"])
@role_required("Administrator", "User")
def purchase():

    user_id = g.current_user_id 

    data = request.get_json() or {}

    fruit_id = data.get("fruit_id")
    quantity = data.get("quantity")

    if fruit_id is None or quantity is None:
        return jsonify({
            "message":"Fruit ID and quantity are required"
        }), 400 

    if (
        not isinstance(fruit_id, int) or isinstance(fruit_id, bool)
        or not isinstance(quantity, int) or isinstance(quantity, bool)
    ):
        return jsonify({
            "message":"Fruit ID and quantity must be integers"
        }), 400

    if fruit_id <= 0 or quantity <= 0:
        return jsonify({
            "message":"Invalid fruit ID or quantity"
        }), 400

    db = MakeConectionDb()

    try:

        fruit_manage = FruitManagement(db)
        invoices_manage = InvoicesManagement(db)

        fruit = fruit_manage.select_fruit(fruit_id)

        if fruit == "fruit_not_found":
            return jsonify({
                "message":"Fruit not found"
            }), 404

        if isinstance(fruit, str):
            return jsonify({
                "message": fruit
            }), 500

        if fruit.stock < quantity:
            return jsonify({
                "message":"Insufficient stock"
            }), 400

        total_price = fruit.price * quantity

        result = invoices_manage.create_new_invoice(
            user_id,
            fruit_id,
            quantity,
            total_price,
            date.today()
        )

        if result is None or isinstance(result, str):
            return jsonify({
                "message": "Error creating invoice",
                "details": result
            }), 500

        stock_result = fruit_manage.modify_fruit(
            fruit_id,
            fruit.fruit_name,
            fruit.price,
            fruit.delivery_date,
            fruit.stock - quantity
        )

        if stock_result != "fruit_modified":
            return jsonify({
                "message": "Error updating fruit stock",
                "details": stock_result
            }), 500

        return jsonify({
            "message":"Purchase successful",
            "invoices_id": result,
            "fruit": fruit.fruit_name,
            "quantity": quantity,
            "total_price": float(total_price),
            "invoices_date": date.today().isoformat()
        }), 201

    finally:
        db.close()