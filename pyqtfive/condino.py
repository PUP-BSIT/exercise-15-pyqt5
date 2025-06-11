from pyqtfive.utils import buffer, clear_screen
from pyqtfive.utils import handle_value_error, handle_unexpected_error

class Condino:
    BACK_TO_MENU_OPTION = 0
    UNSET_OPTION = -1

    def __init__(self):
        self.name = "Ciara Marie Condino"
        self.age = 21
        self.section = "BSIT 2-1"
        
    def show_name(self):
        print(f"Hi! I'm {self.name}.")
        buffer()

    def show_age(self):
        print(f"I am {self.age} years old.")
        buffer()

    def show_section(self):
        print(f"My section is {self.section}.")
        buffer()

    def show_hobby(self):
        print("My hobby is playing online games.")
        buffer()

    def show_favorite_language(self):
        print("Python is my favorite programming language.")
        buffer()

    def menu(self):
        clear_screen()
        choice = self.UNSET_OPTION

        while choice != self.BACK_TO_MENU_OPTION:
            try:
                choice = self.display_choice()
                self.process_choice(choice)
            except ValueError:
                handle_value_error()
            except Exception as e:
                handle_unexpected_error(e)

    def display_choice(self):
        clear_screen()
        print("\n--- Condino's Menu ---")
        print("1. Greet")
        print("2. Show Age")
        print("3. Show Section")
        print("4. Show Hobby")
        print("5. Show Favorite Language")
        print("0. Back to Main Menu")

        return int(input("Enter your choice: "))

    def process_choice(self, choice):
        clear_screen()
        match choice:
            case 1:
                self.show_name()
            case 2:
                self.show_age()
            case 3:
                self.show_section()
            case 4:
                self.show_hobby()
            case 5:
                self.show_favorite_language()
            case 0:
                pass  
            case _:
                print("Invalid choice. Try again.")
                buffer()