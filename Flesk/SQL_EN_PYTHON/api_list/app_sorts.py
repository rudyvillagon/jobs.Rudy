from flask import Flask, request, jsonify
from database.Database_connection import Database
from api_list.sort_users import SortUsers
from api_list.sort_cars import SortCars
from api_list.sort__rentals import SortRentals

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    filters = request.args.to_dict()

    db = Database()

    try:
        sort_data = SortUsers(db)

        users = sort_data.users_sort(filters)

        return jsonify(users)
    
    finally:
        db.close()

@app.route("/cars", methods=["GET"])
def get_cars():
    filters = request.args.to_dict()

    db = Database()
    
    try:
        sort_data = SortCars(db)

        cars = sort_data.cars_sort(filters)

        return jsonify(cars)
    
    finally:
        db.close()

@app.route("/rentals", methods=["GET"])
def get_rentals():
    filters = request.args.to_dict()

    db = Database()

    try:
        sort_data = SortRentals(db)

        users = sort_data.rentals_sort(filters)

        return jsonify(users)
    
    finally:
        db.close()


if  __name__ == "__main__":
    app.run(host="localhost", port=5000,debug=True)
