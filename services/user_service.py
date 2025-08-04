from typing import List

from models.user import User

from utils.utils import make_password


class UserService:
    
    def __init__(self):
        self.logged_user = None
        self.users: List[User] = []
    
    def create_user(self):
        first_name = input()
        last_name = input()
        email = input()
        password = input()
        
        # validate all data
        User.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password)
        )
