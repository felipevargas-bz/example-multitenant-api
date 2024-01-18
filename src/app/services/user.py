# Python Imports

# Flask Imports

# Third-Party Imports
from werkzeug.security import generate_password_hash

# App Imports
from app.models import User, UserSchema
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self):
        super().__init__(User, UserSchema)

    def validate_user(self, username):
        user = self.get_one({"username__eq": username}, dict_format=False)
        if user:
            raise ValueError("El usuario ya existe.")

    def create_admin_user(self, data):
        data["role"] = "Admin"
        return self.create(data)

    def create_user(self, data):
        data["role"] = "User"
        return self.create(data)

    def create(self, data):
        self.validate_user(data["username"])
        password = data.pop("password")
        data["password"] = generate_password_hash(password)

        user = self.model(**data)
        user.save()

    def update(self, user_id, data):
        password = data.pop("password", None)
        if password:
            data["password"] = generate_password_hash(password)
        return super().update(user_id, data)


user_service = UserService()
