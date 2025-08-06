class ProductService:
    def __init__(self, mahsulotlar):
        self.mahsulotlar = mahsulotlar

    def print_products(self):
        if not self.mahsulotlar:
            print("Mahsulotlar ro'yxati bo'sh.")
        else:
            print("Mahsulotlar ro'yxati:")
            for i, mahsulot in enumerate(self.mahsulotlar, start=1):
                nom = mahsulot.get("nom", "Noma'lum")
                narx = mahsulot.get("narx", "Narx ko'rsatilmagan")
                print(f"{i}. Mahsulot nomi: {nom}, Narxi: {narx} so'm")


mahsulotlar = [
    {"nom": "Stol", "narx": 500000},
    {"nom": "Stul", "narx": 200000},
    {"nom": "Shkaf", "narx": 1200000}
]

xizmat = ProductService(mahsulotlar)
xizmat.print_products()