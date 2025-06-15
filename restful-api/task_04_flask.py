#! /usr/bin/python3
"""Simple API with Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Serve a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_users():
    """Return a list of all usernames in the API."""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return API status."""
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Return a user's data by their username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the API."""
    data = request.json

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == '__main__':
    app.run()
