#Import modules from pyqtfive package
from pyqtfive.utils import clear_screen, buffer
#TODO (ARGUELLES): Import a class from a module inside a package
#TODO (CAYA): Import a class from a module inside a package
#TODO (CONDINO): Import a class from a module inside a package
#TODO (CORDOVA): Import a class from a module inside a package
from pyqtfive.gutierrez import Gutierrez

EXIT_OPTION = 0
UNSET_OPTION = -1

# Initialize instances of various classes
#TODO (ARGUELLES): Initialize your imported class
#TODO (CAYA): Initialize your imported class
#TODO (CONDINO): Initialize your imported class
#TODO (CORDOVA): Initialize your imported class
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
            #TODO (ARGUELLES): Call the appropriate function here
            pass
        case 2:
            #TODO (CAYA): Call the appropriate function here
            pass
        case 3:
            #TODO (CONDINO): Call the appropriate function here
            pass
        case 4:
            #TODO (CORDOVA): Call the appropriate function here
            pass
        case 5:
            gutierrez.menu()
        case 0:
            pass
        case _:
            print("Invalid choice. Please try again.")
            buffer()

menu()