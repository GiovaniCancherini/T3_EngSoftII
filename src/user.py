class User:
    def __init__(self, email, name, password):
        self._email = email
        self._name = name
        self._password = password

    # Getters
    def get_email(self):
        return self._email

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    # Setters
    def set_email(self, email):
        self._email = email

    def set_name(self, name):
        self._name = name

    def set_password(self, password):
        self._password = password
