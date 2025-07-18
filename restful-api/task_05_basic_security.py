#! /usr/bin/python3
"""API with Basic Auth and JWT Authentication"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Clé secrète (à changer en production)
app.config['SECRET_KEY'] = 'secret_key'
app.config['JWT_SECRET_KEY'] = 'secret_key'

# Initialisation
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Utilisateurs en mémoire
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ------------------------------------------------------------------------------
# Basic Auth
# ------------------------------------------------------------------------------
@auth.verify_password
def verify(username, password):
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return users[username]
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ------------------------------------------------------------------------------
# JWT Auth
# ------------------------------------------------------------------------------
@app.route('/login', methods=['POST'])
def login():
    """Login to receive a JWT access token."""
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    identity = {"username": username, "role": user["role"]}
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Protect route for admin users only."""
    current_user = get_jwt_identity()
    if current_user and current_user["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


# ------------------------------------------------------------------------------
# Error handlers for JWT
# ------------------------------------------------------------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err, payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ------------------------------------------------------------------------------
# Run application
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()
