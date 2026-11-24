import jwt
import os
from datetime import datetime, timedelta, timezone

class JWTManager:

    def __init__(self, private_key, public_key, algorithm, access_expiration, refresh_expiration):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm
        self.access_expiration = access_expiration
        self.refresh_expiration = refresh_expiration

    def encode(self, data, expires_in):

        payload = {
            **data,
            "exp": datetime.now(timezone.utc) + timedelta(seconds= expires_in)
        }

        try:
            return jwt.encode(
                payload,
                self.private_key,
                algorithm=self.algorithm
            )

        except (jwt.PyJWKError, TypeError) as error:
            print(f"Error generating token: {error}")
            return None

    def decode(self, token):

        try:
            return jwt.decode(
                token,
                self.public_key,
                algorithms=[self.algorithm]
            )

        except jwt.InvalidTokenError as error:
            print(f"Invalid token: {error}")
            return None

    def generate_tokens(self, user_id, role):

        access_token = self.encode(
            {
                "id": user_id,
                "role": role,
                "type": "access"
            },
            self.access_expiration
        )

        refresh_token = self.encode(
            {
                "id": user_id,
                "role": role,
                "type": "refresh",
            },
            self.refresh_expiration
        )

        return access_token, refresh_token

    def decode_token(self, token, expect_type):

        decoded = self.decode(token)

        if decoded is None or decoded.get("type") != expect_type:
            return None 

        return decoded

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, "private.pem"), "r") as file:
    private_key = file.read()

with open(os.path.join(base_dir, "public_key.pem"), "r") as file:
    public_key = file.read()

jwt_manager = JWTManager(
    private_key= private_key,
    public_key= public_key,
    algorithm= "RS256",
    access_expiration= 900,
    refresh_expiration= 604800
)