from typing import List

from models.user import User

from utils.utils import make_password


class UserService:
    
    def __init__(self):
        self.logged_user = None
        self.users: List[User] = []
    
    def create_user(self):
        first_name = input("Ismingizni kiriting: ").strip().capitalize()
        last_name = input("Familiyangizni kirting: ").strip().capitalize()
        email = input("Email manzilingizni kiriting: (masalan: vali@gmail.com)").strip().lower()
        password = input("Parol kiriting:")
        if len(password) < 6:
            print("password kamida 6 ta harfdan iborat bo'lishi kerak: ")
        else:
            print("Password xato: ")
      
      
        # validate all data
        User.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password)
        )
