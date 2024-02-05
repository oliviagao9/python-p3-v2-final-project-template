# lib/cli.py
from helpers import *
import time

def greeting():
    print("Hi there welcome to Olivia Florist Inventory Management System")

def main():
    cli_menu_flag = True
    while cli_menu_flag == True:
        menu()
        choice = input("> ")

        if choice == "1":
            view_current_inventory()
            return_menu_option()

        elif choice == "2":
            add_inventory()
            return_menu_option()

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            pass

        elif choice == "6":
            exit_program()

        else:
            print("Please Enter a valid choice from 1 - 6")

def return_menu_option():
    time.sleep(1)
    print("If you want to go back to previous menu, please enter 1")
    print("If you want to exit the application, please enter 2")
    user_choice = input("> ")

    if user_choice == "1":
        time.sleep(0.5)
        main()

    elif user_choice == "2":
        exit_program()

if __name__ == "__main__":
    main()
