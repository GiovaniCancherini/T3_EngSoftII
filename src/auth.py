from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)


class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password


class AuthenticationService:
    def __init__(self):
        self.users = []

    def register_user(self, email, name, password):
        user = User(email, name, password)
        self.users.append(user)

    def authenticate(self, email, password):
        user = next((user for user in self.users if user.email == email), None)
        if user and user.password == password:
            return True
        return False


class AuthorizationService:
    def __init__(self):
        self.user_roles = {}

    def assign_role(self, email, role):
        self.user_roles[email] = role

    def authorize(self, email, role):
        user_role = self.user_roles.get(email)
        if user_role == role:
            return True
        return False


auth_service = AuthenticationService()
auth_service.register_user("user1@example.com", "User 1", "password1")
auth_service.register_user("user2@example.com", "User 2", "password2")

authz_service = AuthorizationService()
authz_service.assign_role("user1@example.com", "admin")
authz_service.assign_role("user2@example.com", "student")


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if auth_service.authenticate(email, password):
        access_token = create_access_token(identity=email)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = request.identity
    role = request.args.get('role')

    if authz_service.authorize(current_user, role):
        return jsonify({'message': 'Access granted'}), 200

    return jsonify({'error': 'Access denied'}), 403


if __name__ == '__main__':
    app.run()
