from uuid import uuid4

class Product:

    def __init__(self, name: str, category: str, price: float, is_stock: bool, product_id: str,):
        self.product_id = product_id or str(uuid4())
        self.name = name
        self.category = category
        self.price = price
        self.is_stock = is_stock

    def to_dict(self) -> dict:
        return{
            'product id': self.product_id,
            'product name': self.name,
            'product category': self.category,
            'product price': self.price,
            'product in stock': self.is_stock
        }
 
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            product_id = data['product id'],
            name = data['product name'],
            category = data['product category'],
            price = data['product price'],
            is_stock = data['product in stock']
        )        