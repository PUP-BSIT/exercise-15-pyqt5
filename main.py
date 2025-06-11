#Import modules from pyqtfive package
from pyqtfive.utils import clear_screen, buffer
from pyqtfive.utils import handle_value_error, handle_unexpected_error
from pyqtfive.arguelles import Arguelles
from pyqtfive.caya import Caya
from pyqtfive.condino import Condino
from pyqtfive.cordova import Cordova
from pyqtfive.gutierrez import Gutierrez

EXIT_OPTION = 0
UNSET_OPTION = -1

# Initialize instances of various classes
arguelles = Arguelles()
caya = Caya()
condino = Condino()
cordova = Cordova()
gutierrez = Gutierrez()

def menu():
    clear_screen()
    choice = UNSET_OPTION

    while choice != EXIT_OPTION:
        try:
            choice = display_choice()
            process_choice(choice)
        except ValueError:
            handle_value_error()
        except Exception as e:
            handle_unexpected_error(e)
            
def display_choice():
    clear_screen()
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
            condino.menu()
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