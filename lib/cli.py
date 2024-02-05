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
            view_current_inventory()
            update_inventory()
            return_menu_option()

        elif choice == "4":
            view_current_inventory()
            delete_inventory()
            return_menu_option()

        elif choice == "5":
            order_menu_option()

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

def order_menu_option():
    print("Please select an option for Order:")
    print("1. Place an New Order")
    print("2. Edit an Existing Order")
    print("3. Delete Order")
    print("4. Exit")
    user_choice = input("> ")
    
    if user_choice == "1":
        view_current_inventory()
        add_order()
        
    elif user_choice == "2":
        pass
    elif user_choice == "3":
        pass
    elif user_choice == "4":
        exit_program()
    else:
        print("Please Enter a valid choice from 1 - 4")
        order_menu_option()

if __name__ == "__main__":
    main()
