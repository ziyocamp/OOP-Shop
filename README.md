# OOP-Shop

## Project file structure

```
shop_project/
├── data/
│   └── db.json                  # Mahsulotlar, foydalanuvchilar, buyurtmalar saqlanadigan JSON file
│
├── models/
│   ├── __init__.py
│   ├── product.py               # Mahsulot modeli
│   ├── user.py                  # Foydalanuvchi modeli
│   └── order.py                 # Buyurtma modeli
│
├── services/
│   ├── __init__.py
│   ├── database.py              # JSON bilan o'qish/yozish logikasi
│   ├── product_service.py       # Mahsulotlar bilan ishlash (qo‘shish, o‘chirish, o‘zgartirish)
│   ├── user_service.py          # Foydalanuvchilar bilan ishlash
│   └── order_service.py         # Buyurtmalar logikasi
│
├── interfaces/
│   ├── __init__.py
│   ├── main_menu.py             # Rich yordamida asosiy menyu interfeysi
│   └── forms.py                 # Ma'lumot kiritish interfeyslari (input dialogs)
│
├── utils/
│   ├── __init__.py
│   └── validators.py            # Input tekshiruvlar, formatlash funksiyalari
│
├── main.py                      # Dastur boshlanish nuqtasi
└── requirements.txt             # Rich kutubxonasi va boshqa kerakli modullar
```
