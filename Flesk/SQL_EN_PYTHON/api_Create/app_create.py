from flask import Flask, request, jsonify
from database.Database_connection import Database
from api_Create.Add_user import AddUser
from api_Create.Add_Automovil import NewVehicle
from api_Create.Add_new_rent import NewRental

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def add_user_api():
    request_body = request.json

    db = Database()

    try:
        users = AddUser(db)

        users.add_user(request_body)

        return jsonify(message= "User has been Created"), 201
    finally:
        db.close()


@app.route("/cars", methods=["POST"])
def add_automovil_api():

    request_body = request.json

    db = Database()

    try:
        n_vehicle = NewVehicle(db)

        n_vehicle.add_automovil(request_body)

        return jsonify(message= "Car has been added"), 201
    finally:
        db.close()



@app.route("/rentals", methods=["POST"])
def new_rent_car_api():

    request_body = request.json

    db = Database()

    try:
        new_rent = NewRental(db)

        new_rent.new_rent_car(request_body)

        return jsonify(message= "New Rental added"), 201
    finally:
        db.close()




if  __name__ == "__main__":
    app.run(host="localhost", port=5000,debug=True)