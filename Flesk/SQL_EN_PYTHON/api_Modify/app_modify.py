from flask import Flask, request, jsonify
from database.Database_connection import Database
from api_Modify.Status_change_car import ChangeStatusCar
from api_Modify.Status_change_user import ChangeStatusUser
from api_Modify.Complet_car_return import CarReturn 
from api_Modify.Disable_rent_car import ChangeCarStatusDisable
from api_Modify.Defaulter_user import ChangeDefaulterUser

app = Flask(__name__)

@app.route("/cars", methods=["PATCH"])
def change_status_car_api():
    request_body = request.json

    db= Database()

    try:
        new_status_car = ChangeStatusCar(db)

        result = new_status_car.change_car_status(request_body)

        if result == "car_not_found":
            return jsonify(message="The car is not found."), 404
        elif result == "car_already_has_that_status":
            return jsonify(message="The has already that status."), 400

        else:
            return jsonify(message="Status of the Car has been Change"), 201
    finally:
        db.close()



@app.route("/users", methods=["PATCH"])
def change_status_user_api():
    request_body = request.json

    db = Database()

    try:
        new_status_user = ChangeStatusUser(db)

        result = new_status_user.change_user_status(request_body)

        if result == "user_not_exist":
            return jsonify(message="The user does not exist."), 404
        elif result == "user_already_has_that_status":
            return jsonify(message="The user already has that status."), 409

        else:
            return jsonify(message= "Status of the User has been Change"), 201
    finally:
        db.close()



@app.route("/cars/return", methods=["PATCH"])
def complet_car_return_api():
    request_body = request.json

    db = Database()

    try:
        return_car = CarReturn(db)

        result = return_car.car_return(request_body)

        if result == "invoice_not_exist":
            return jsonify(message="The invoice does not exist."), 404
        elif result == "vehicle_already_returned":
            return jsonify(message="the vehicle has already been returned."), 409

        else:
            return jsonify(message= "The car has been returned"), 201
    finally:
        db.close()



@app.route("/cars/disable", methods=["PATCH"])
def disable_car_api():
    request_body = request.json

    db = Database()

    try:
        disable_c = ChangeCarStatusDisable(db)

        result = disable_c.disable_car(request_body)

        if result == "car_not_exist":
            return jsonify(message="The car is not found."), 404
        elif result == "car_already_retired":
            return jsonify(message="The car is already retired."), 409

        else:
            return jsonify(message= "The car has been returned"), 201
    finally:
        db.close()



@app.route("/users/defaulter", methods=["PATCH"])
def change_defaulter_user_api():
    request_body = request.json

    db = Database()

    try:
        defaulter_user = ChangeDefaulterUser(db)

        result = defaulter_user.change_user_defaulter(request_body)

        if result == "user_has_no_rentals":
            return jsonify(message="The user has no rentals."), 404

        else:
            return jsonify(message= "The user has been flagged as defaulter."), 201
    finally:
        db.close()


if  __name__ == "__main__":
    app.run(host="localhost", port=5000,debug=True)