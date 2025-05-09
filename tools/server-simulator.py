#!/usr/bin/env python3

from flask import Flask, request, jsonify
import uuid

"""
This server simulates the behavior of a real API server
and provides endpoints for testing purposes.
"""

app = Flask(__name__)

# In-memory storage for pets
pets = {
    1: {"id": 1, "name": "Dog", "status": "available"},
    2: {"id": 2, "name": "Cat", "status": "sold"},
    3: {"id": 3, "name": "Fish", "status": "pending"},
}

@app.route("/v2/pet", methods=["POST"])
def add_new_pet():
    """Add a new pet."""
    pet_data = request.json
    if not pet_data or "id" not in pet_data:
        return jsonify({"error": "Invalid pet data"}), 400
    pet_id = uuid.uuid4().int
    pet_data["id"] = pet_id
    pets[pet_id] = pet_data
    return jsonify(pet_data), 200

@app.route("/v2/pet/<int:pet_id>", methods=["GET"])
def find_pet_by_id(pet_id):
    """Find a pet by ID."""
    pet = pets.get(pet_id)
    if pet:
        return jsonify(pet), 200
    return jsonify({"error": "Pet not found"}), 404

@app.route("/v2/pet/<int:pet_id>", methods=["DELETE"])
def delete_pet_by_id(pet_id):
    """Delete a pet by ID."""
    if pet_id in pets:
        del pets[pet_id]
        return jsonify({"message": "Pet deleted"}), 200
    return jsonify({"error": "Pet not found"}), 404


if __name__ == "__main__":
    app.run(port=5000)
