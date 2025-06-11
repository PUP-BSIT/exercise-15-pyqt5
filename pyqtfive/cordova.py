from pyqtfive.utils import clear_screen, buffer

class Cordova:
    BACK_TO_MENU_OPTION = 0
    UNSET_OPTION = -1

    def __init__(self):
        self.name = "Aron Stephen S. Cordova"
        self.age = 20
        self.section = "BSIT 2-1"

    def greet(self):
        print(f"Salut! Je suis {self.name}.")
        print(f"Hello! I'm {self.name}.")
        buffer()

    def show_age(self):
        print(f"My age is {self.age}.")
        buffer()

    def show_section(self):
        print(f"My section is {self.section}.")
        buffer()

    def show_hobby(self):
        print("I enjoy reading speculative biology themed books.")
        buffer()

    def show_favorite_language(self):
        print("My favorite language is COBOL.")
        buffer()

    def menu(self):
        clear_screen()
        choice = self.UNSET_OPTION

        while choice != self.BACK_TO_MENU_OPTION:
            choice = self.display_choice()
            self.process_choice(choice)
            clear_screen()

    def display_choice(self):
        print("--- Cordova's Menu ---")
        print("1. Greet")
        print("2. Show Age")
        print("3. Show section")
        print("4. Show hobby")
        print("5. Show favorite language")
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
                self.show_section()
            case 4:
                self.show_hobby()
            case 5:
                self.show_favorite_language()
            case 0:
                pass
            case _:
                print("Invalid choice.")
                buffer()