
# import interfaces
from interfaces.main_menu import home_manu, main_menu

# import services
from services.product_service import ProductService
from services.user_service import UserService


def main() -> None:
    user_service = UserService()

    while True:
        home_manu()

        choice = input("> ")
        if choice == '1':
            user_service.login_user()

            while user_service.logged_user:
                product_service = ProductService(user_service.db.data['products'])
                main_menu()

                choice = input("> ")
                if choice == '1':
                    product_service.print_products()
                    product_id = input("qaysi mahsulotni harid qilmoqchisiz: ")
                    
                elif choice == '2':
                    pass
                elif choice == '3':
                    user_service.logged_user = None

        elif choice == '2':
            user_service.create_user()
        elif choice == '3':
            exit()
        else:
            print("Siz xato menu tanladigniz.")

if __name__ == "__main__":
    main()
