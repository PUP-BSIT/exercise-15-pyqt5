#Import modules from pyqtfive package
from pyqtfive.utils import clear_screen, buffer
from pyqtfive.arguelles import Arguelles
from pyqtfive.caya import Caya
#TODO (CONDINO): Import a class from a module inside a package
from pyqtfive.cordova import Cordova
from pyqtfive.gutierrez import Gutierrez

EXIT_OPTION = 0
UNSET_OPTION = -1

# Initialize instances of various classes
arguelles = Arguelles()  # Initialize Norlan Arguelles' class
caya = Caya()
#TODO (CONDINO): Initialize your imported class
cordova = Cordova()
gutierrez = Gutierrez()

def menu():
    clear_screen()
    choice = UNSET_OPTION

    while choice != EXIT_OPTION:
        choice = display_choice()
        process_choice(choice)
        clear_screen()

def display_choice():
    print("=== Team Member Menu ===")
    print("1 - Norlan Arguelles")
    print("2 - Karl Caya")
    print("3 - Ciara Marie Condino")
    print("4 - Aron Stephen Cordova")
    print("5 - King Andrei Gutierrez")
    print("0 - Exit")
        
    return int(input("\nSelect a team member: "))

def process_choice(choice):
    clear_screen()   
    match choice:
        case 1:
            arguelles.menu()
        case 2:
            caya.menu()
        case 3:
            #TODO (CONDINO): Call the appropriate function here
            pass
        case 4:
            cordova.menu()
        case 5:
            gutierrez.menu()
        case 0:
            pass
        case _:
            print("Invalid choice. Please try again.")
            buffer()

menu()