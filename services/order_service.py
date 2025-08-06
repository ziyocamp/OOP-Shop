from models.order import Order
from models.product import Product
from models.user import User

class OrderService:
    def __init__(self):
        self.orders = []

    def create_order(self, user: User, products: list[Product]) -> None:
        order = Order(user=user, products=products)
        self.orders.append(order)
        print("Buyurtma muvaffaqiyatli yaratildi.")

    def get_orders(self) -> list:
        return self.orders

    def print_check(self):
        if not self.orders:
            print("Hozircha hech qanday buyurtma mavjud emas.")
            return

        order = self.orders[-1]
        print("\n=== CHEK ===")
        print(f"Foydalanuvchi: {order.user.name}")
        print("Mahsulotlar:")
        total = 0
        for product in order.products:
            print(f"- {product.name}: {product.price} so'm")
            total += product.price
        print(f"Jami: {total} so'm\n")
