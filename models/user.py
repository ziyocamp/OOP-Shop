from uuid import uuid4


class User:

    def __init__(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            user_id: str | None = None
        ):
        self.user_id = user_id or str(uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def to_dict(self) -> dict:
        return {
            'id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }
    
    @classmethod
    def create_user(cls, first_name, last_name, email, password, user_id=None):
        return cls(
            first_name,
            last_name,
            email,
            password,
            user_id
        )
