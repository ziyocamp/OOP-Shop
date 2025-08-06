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
        try:
            with open(self.filename, "r") as f:
                self.data = json.load(f)
        except json.decoder.JSONDecodeError:
            pass

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def create_user(self, user):
        self.data["users"].append(user)
        self.save_data()

    def get_user(self, email, password):
        for user in self.data['users']:
            if user['email'] == email and user['password'] == password:
                return user

    def create_product(self, product):
        self.data["products"].append(product)
        self.save_data()

    def create_order(self, order):
        self.data["orders"].append(order)
        self.save_data()
