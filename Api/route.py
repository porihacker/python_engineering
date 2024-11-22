from flask import Flask, jsonify, request

app = Flask(__name__)

users = []


# Route to create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = {"id": len(users) + 1, "name": data["name"]}
    users.append(user)
    return jsonify({"message": "User created!"}), 201


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            return jsonify({"message": "User updated!"}), 200
    return jsonify({"error": "User not found!"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": f"{user['name']} has been deleted"})
    return jsonify({"error": "User not dound!"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
