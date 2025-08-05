"""
services/database.py

Ushbu modul ma'lumotlar bazasi sifatida ishlatiladigan JSON fayl bilan ishlaydi.
Foydalanuvchilar, mahsulotlar va buyurtmalarni saqlaydi va boshqaradi.

Class: Database

Attributes:
- filename: JSON fayl manzili
- data: Dasturdagi barcha ma'lumotlar (users, products, orders)

Methods:
- load_data(): JSON fayldan ma'lumotlarni o'qiydi
- save_data(): Ma'lumotlarni faylga yozadi
- create_user(user): Foydalanuvchi qo'shadi
- create_product(product): Mahsulot qo'shadi
- create_order(order): Buyurtma qo'shadi
"""

import json

class Database:
    def __init__(self, filename = 'data/db.json'):
        self.filename = filename
        self.data = {
            "users": [],
            "products": [],
            "orders": []
        }
        self.load_data()

    def load_data(self):
        with open(self.filename, "r") as f:
            self.data = json.load(f)

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def create_user(self, user):
        self.data["users"].append(user)
        self.save_data()

    def create_product(self, product):
        self.data["products"].append(product)
        self.save_data()

    def create_order(self, order):
        self.data["orders"].append(order)
        self.save_data()
