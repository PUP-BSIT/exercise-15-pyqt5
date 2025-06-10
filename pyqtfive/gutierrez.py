from pyqtfive.utils import clear_screen, buffer

class Gutierrez:
    BACK_TO_MENU_OPTION = 0
    UNSET_OPTION = -1

    def __init__(self):
        self.name = "King Andrei Gutierrez"
        self.age = 20
        self.game = "Wuthering Waves"

    def greet(self):
        print(f"Hello, I'm {self.name}.")
        buffer()

    def show_age(self):
        print(f"I am {self.age} years old.")
        buffer()

    def show_favorite_game(self):
        print(f"My favorite online game is {self.game}.")
        buffer()

    def show_double_age(self):
        print(f"My age doubled is {self.age * 2}.")
        buffer()

    def show_initials(self):
        print("Initials: KAG.")
        buffer()

    def menu(self):
        clear_screen()
        choice = self.UNSET_OPTION

        while choice != self.BACK_TO_MENU_OPTION:
            choice = self.display_choice()
            self.process_choice(choice)
            clear_screen()

    def display_choice(self):
        print("\n--- Hello, Welcome to Gutierrez Menu ---")
        print("1. Greet")
        print("2. Show Age")
        print("3. Show Favorite Language")
        print("4. Show Double Age")
        print("5. Show Initials")
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
                self.show_favorite_game()
            case 4:
                self.show_double_age()
            case 5:
                self.show_initials()
            case 0:
                pass
            case _:
                print("Invalid choice.")
                buffer()