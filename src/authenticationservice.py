from user import User


class AuthenticationService:
    def __init__(self):
        self._users = []

    def register_user(self, user_data):
        email = user_data.get('email')
        name = user_data.get('name')
        password = user_data.get('password')

        # Verifica se o e-mail já está registrado
        if self._find_user_by_email(email):
            return False

        # Cria um novo usuário e o adiciona à lista de usuários
        user = User(email, name, password)
        self._users.append(user)
        return True

    def authenticate(self, email, password):
        user = self._find_user_by_email(email)
        if user and user.get_password() == password:
            return True
        return False

    def _find_user_by_email(self, email):
        for user in self._users:
            if user.get_email() == email:
                return user
        return None
