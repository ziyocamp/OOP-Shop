from uuid import uuid4


class Order:
    def __init__(self, user, products, order_id: str | None = None):
        self.user = user
        self.products = products 
        self.order_id = order_id or str(uuid4())

    def to_dict(self):
        """
        Bu metod Order obyektini dict formatga o'tkazadi
        """
        return {
            'user': self.user,
            'products': self.products,
            'id': self.order_id 
        }

    @classmethod
    def from_dict(cls, data):
        """
        Bu classmethod dictionarylardan dan Order obyekti yasaydi
        """
        return cls(
            user=data.get('user'),
            products=data.get('products'),
            order_id=data.get('order_id')
        )
