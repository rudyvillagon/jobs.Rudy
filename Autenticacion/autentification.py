from flask import Blueprint, request, jsonify
from user_repository import user_repository
from jwt_manager import jwt_manager

users_veri = Blueprint("user-service", __name__)

@users_veri.route("/login", methods= ["POST"])
def login():
    data = request.get_json()
    user_name = data.get("user_name")
    password = data.get("password")

    if user_name is None or password is None:
        return jsonify(error= "Username and password are required"), 400

    user = user_repository.get_by_credentials(user_name, password)
    if user is None:
        return jsonify(error= "Invalid username or password"), 401

    access_token, refresh_token = jwt_manager.generate_tokens(user.id)
    return jsonify(access_token= access_token, refresh_token= refresh_token)

@users_veri.route("/me")
def me():
    token = request.headers.get("Authorization")
    if token is None:
        return jsonify(error="Missing Authorization header"), 401

    token = token.replace("Bearer ", "")
    decoded = jwt_manager.decode_token(token, "access")
    if decoded is None:
        return jsonify(error= "Invalid or expired access token"), 401

    user = user_repository.get_by_id(decoded["id"])
    if user is None:
        return jsonify(error= "User not found"), 404

    return jsonify(id= user.id, user_name= user.user_name)