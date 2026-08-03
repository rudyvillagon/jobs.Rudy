from flask import Flask, request, jsonify
from database.Database_connection import Database
from api_Modify.Status_change_car import ChangeStatusCar
from api_Modify.Status_change_user import ChangeStatusUser
from api_Modify.Complet_car_return import CarReturn 
from api_Modify.Disable_rent_car import ChangeCarStatusDisable
from api_Modify.Defaulter_user import ChangeDefaulterUser

app = Flask(__name__)

@app.route("/cars", methods=["PACTH"])
def change_status_car_api():
    request_body = request.json

    db= Database()

    try:
        new_status_car = ChangeStatusCar(db)

        new_status_car.change_car_status(request_body)

        return jsonify(message= "Status of the Car has been Change"), 201
    finally:
        db.close()



@app.route("/users", methods=["PACTH"])
def change_status_user_api():
    request_body = request.json

    db = Database()

    try:
        new_status_user = ChangeStatusUser(db)

        new_status_user.change_user_status(request_body)

        return jsonify(message= "Status of the User has been Change"), 201
    finally:
        db.close()



@app.route("/cars/return", methods=["PATCH"])
def complet_car_return_api():
    request_body = request.json

    db = Database()

    try:
        return_car = CarReturn(db)

        return_car.car_return(request_body)

        return jsonify(message= "The car has been returned"), 201
    finally:
        db.close()



@app.route("/cars/disable", methods=["PATCH"])
def disable_car_api():
    request_body = request.json

    db = Database()

    try:
        disable_c = ChangeCarStatusDisable(db)

        disable_c.disable_car(request_body)

        return jsonify(message= "The car has been returned"), 201
    finally:
        db.close()



@app.route("/users/defaulter", methods=["PACTH"])
def change_status_user_api():
    request_body = request.json

    db = Database()

    try:
        defaulter_user = ChangeDefaulterUser(db)

        defaulter_user.change_user_defaulter(request_body)

        return jsonify(message= "The user has been flagged as defaulter."), 201
    finally:
        db.close()


if  __name__ == "__main__":
    app.run(host="localhost", port=5000,debug=True)