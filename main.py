
# import interfaces
from interfaces.main_menu import home_manu

# import services
from services.user_service import UserService


def main() -> None:
    user_service = UserService()

    home_manu()

    choice = input("> ")
    if choice == '1':
        pass
    elif choice == '2':
        user_service.create_user()
    elif choice == '3':
        exit
    else:
        print("Siz xato menu tanladigniz.")

if __name__ == "__main__":
    main()
