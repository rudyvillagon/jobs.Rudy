from functools import wraps
from flask import request, jsonify, g
from  jwt_manager import jwt_manager
def role_required(*required_role):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            auth_header = request.headers.get("Authorization")

            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({
                    "message": "Authorization token is missing"
                }), 401 

            token = auth_header.split(" ", 1)[1]

            decoded = jwt_manager.decode_token(
                token, 
                "access"
            )

            if decoded is None:
                return jsonify({
                    "message": "Invalid or expired token"
                }), 401

            user_role = decoded.get("role")

            if user_role not in required_role:
                return jsonify({
                    "message": "You do not have permission"
                }), 403

            g.current_user_id = decoded.get("id")
            g.current_user_role_ = user_role

            return function(*args, **kwargs)

        return wrapper

    return decorator