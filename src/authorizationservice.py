class AuthorizationService:
    def __init__(self):
        self._user_roles = {}

    def assign_role(self, user_email, role):
        self._user_roles[user_email] = role

    def authorize(self, user_email, role):
        user_role = self._user_roles.get(user_email)
        if user_role == role:
            return True
        return False
