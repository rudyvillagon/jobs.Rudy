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

        result = users.add_user(request_body)

        if result is False:
            return jsonify(message= "The email is already in use"),400

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

        result = new_rent.new_rent_car(request_body)

        if result == "user_not_exist":
            return jsonify(message="The user does not exist."), 404
        
        if result == "user_not_active":
            return jsonify(message="The user is not active."), 400
        
        if result == "The car_not_exist":
            return jsonify(message="The car does not exist."), 404
        
        if result == "car_not_available":
            return jsonify(message="the car is not available."), 409

        else:
            return jsonify(message= "New Rental added"), 201
    finally:
        db.close()




if  __name__ == "__main__":
    app.run(host="localhost", port=5000,debug=True)