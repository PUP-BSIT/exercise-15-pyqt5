import os

def buffer():
    input("\nPress Enter to continue...")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')