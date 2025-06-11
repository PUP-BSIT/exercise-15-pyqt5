from pyqtfive.utils import buffer, clear_screen

class Arguelles:
    EXIT_OPTION = 0
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
    
    def favorite_movie(self):
        print(f"My favorite movie is {self.movie}.")
        buffer()
        
    def favorite_game(self):
        print(f"My favorite game is League of Legends.")
        buffer()
        
    def show_birthday(self):
        print("My birthday is December 10, 2004")
        buffer()
    
    def menu(self):
        clear_screen()
        choice = self.UNSET_OPTION
        
        while choice != self.EXIT_OPTION:
            choice = self.display_get_choice()
            self.process_choice(choice)
            
    def display_get_choice(self):
        clear_screen()
        print("1. Greet")
        print("2. Show Age")
        print("3. Favorite Movie")
        print("4. Favorite Game")
        print("5. Birthday")
        print("0. Exit")
               
        return int(input("Enter your choice: "))
    
    def process_choice(self, choice):
        clear_screen()
        match choice:
            case 1:
                self.greet()
            case 2:
                self.show_age()
            case 3:
                self.favorite_movie()
            case 4:
                self.favorite_game()
            case 5:
                self.show_birthday()
            case 0:
                pass
            case _:
                print("Invalid choice, please try again.")
                buffer()