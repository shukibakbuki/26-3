from flask import Flask, request, jsonify

app = Flask(__name__)

# 🚨 Hardcoded credentials (bad practice)
USERS = {
    "admin": "password123",
    "guest": "guest"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) == password:
        return jsonify({
            "message": "Login successful",
            "token": "insecure-token-123"  # 🚨 static token (insecure)
        })
    else:
        return jsonify({
            "message": "Invalid credentials"
        }), 401

@app.route('/secret-data', methods=['GET'])
def secret_data():
    # 🚨 token is passed via query string (bad practice)
    token = request.args.get("token")
    if token == "insecure-token-123":
        return jsonify({
            "secret": "This is confidential data only authorized users should see."
        })
    else:
        return jsonify({
            "error": "Unauthorized"
        }), 403

if __name__ == '__main__':
    app.run(debug=True)
