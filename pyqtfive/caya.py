from pyqtfive.utils import clear_screen, buffer
from pyqtfive.utils import handle_value_error, handle_unexpected_error

class Caya:
    BACK_TO_MENU_OPTION = 0
    UNSET_OPTION = -1

    def __init__(self):
        self.name = "Karl Christian M. Caya"
        self.age = 20
        self.band = "Wave To Earth"

    def greet(self):
        print(f"Hello! I'm {self.name}.")
        buffer()

    def show_age(self):
        print(f"My age is {self.age}.")
        buffer()

    def show_band(self):
        print(f"My favorite band is {self.band}.")
        buffer()
        
    def show_dream(self):
        print("I want to travel the world.")
        buffer()

    def show_hobby(self):
        print("I love singing.")
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
        print("--- Caya's Menu ---")
        print("1. Greet")
        print("2. Show Age")
        print("3. Show Favorite Band")
        print("4. Show Dream")
        print("5. Show Hobby")
        print("0. Back to Main Menu")
        
        return int(input("\nEnter your choice: "))
    
    def process_choice(self, choice):
        clear_screen()
        match choice:
            case 1:
                self.greet()
            case 2:
                self.show_age()
            case 3:
                self.show_band()
            case 4:
                self.show_dream()
            case 5:
                self.show_hobby()
            case 0:
                pass
            case _:
                print("Invalid choice.")
                buffer()