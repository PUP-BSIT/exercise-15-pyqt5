import os

def buffer():
    input("\nPress Enter to continue...")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_value_error():
    clear_screen()
    print("Invalid input. Please enter a number.")
    buffer()

def handle_unexpected_error(e):
    clear_screen()
    print(f"An unexpected error occurred: {e}")
    buffer()