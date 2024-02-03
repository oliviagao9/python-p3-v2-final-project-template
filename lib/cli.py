# lib/cli.py
import time
from helpers import *

def greeting():
    print("Hi there welcome to Olivia Florist Inventory Management System")

def main():
    cli_menu_flag = True
    while cli_menu_flag == True:
        menu()
        choice = input("> ")

        if choice == "1":
            view_current_inventory()
            cli_menu_flag = False
            return_menu_option()

        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            exit_program()
        else:
            print("Please Enter a valid choice from 1 - 4")


def menu():
    print("Please select an option:")
    print("1. View Current Inventory")
    print("2. Update Inventory")
    print("3. Place Order")
    print("4. Exit")

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

def update_inventory_menu():
    print("Please select an option:")
    print("1. Edit Current Inventory")
    print("2. Add New Inventory")
    print("3. Delete Inventory")
    print("4. Exit")

if __name__ == "__main__":
    main()
