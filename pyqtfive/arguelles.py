from pyqtfive.utils import buffer, clear_screen
from pyqtfive.utils import handle_value_error, handle_unexpected_error

class Arguelles:
    BACK_TO_MENU_OPTION = 0
    UNSET_OPTION = -1
    
    def __init__(self):
        self.name = "Norlan C. Arguelles"
        self.age = 20
        self.movie = "The Hunger Games: Catching Fire"
    
    def greet(self):
        print(f"Hello, my name is {self.name}.")
        buffer()
        
    def show_age(self):
        print(f"I am {self.age} years old.")
        buffer()
    
    def show_favorite_movie(self):
        print(f"My favorite movie is {self.movie}.")
        buffer()
        
    def show_favorite_game(self):
        print("My favorite game is League of Legends.")
        buffer()
        
    def show_birthday(self):
        print("My birthday is December 10, 2004")
        buffer()
    
    def menu(self):
        clear_screen()
        choice = self.UNSET_OPTION

        while choice != self.BACK_TO_MENU_OPTION:
            try:
                choice = self.display_get_choice()
                self.process_choice(choice)
            except ValueError:
                handle_value_error()
            except Exception as e:
                handle_unexpected_error(e)
            
    def display_get_choice(self):
        clear_screen()
        print("--- Welcome to Arguelles Menu ---")
        print("1. Greet")
        print("2. Show Age")
        print("3. Favorite Movie")
        print("4. Favorite Game")
        print("5. Birthday")
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
                self.show_favorite_movie()
            case 4:
                self.show_favorite_game()
            case 5:
                self.show_birthday()
            case 0:
                pass
            case _:
                print("Invalid choice, please try again.")
                buffer()