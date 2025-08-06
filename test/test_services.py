from services.product_service import ProductService


mahsulotlar = [
    {"nom": "Stol", "narx": 500000},
    {"nom": "Stul", "narx": 200000},
    {"nom": "Shkaf", "narx": 1200000}
]

xizmat = ProductService(mahsulotlar)
xizmat.print_products()
