from typing import List

from models.user import User

from utils.utils import make_password
from utils.validators import validate_name, validate_email

from services.database import Database


class UserService:
    
    def __init__(self):
        self.logged_user = None
        self.db = Database()
        self.users: List[User] = []
    
    def create_user(self):
        first_name = input("Ismingizni kiriting: ").strip().capitalize()
        last_name = input("Familiyangizni kirting: ").strip().capitalize()
        email = input("Email manzilingizni kiriting (masalan: vali@gmail.com): ").strip().lower()
        password = input("Parol kiriting: ")

        if not validate_name(first_name):
            print("First Name xato kiritgansiz.")
        elif not validate_name(last_name):
            print("Last Name xato kiritgansiz.")
        elif not validate_email(email):
            print("Email xato kiritgansiz.")
        else:
            user = User.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password)
            )
            self.db.create_user(user.to_dict())

            print("Siz muvaffaqiyatli royxatdan otdingiz.")

    def login_user(self):
        email = input("Email manzilingizni kiriting (masalan: vali@gmail.com): ").strip().lower()
        password = input("Parol kiriting: ")

        if not validate_email(email):
            print("Email xato kiritgansiz.")

        user_data = self.db.get_user(email, make_password(password))
        
        if user_data:
            self.logged_user = User.create_user(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                password=user_data['password'],
                user_id=user_data['id'],
            )
            print("Siz muvaffaqiyatli kirdingiz.")
        else:
            print("Bunda user mavjud emas.")
