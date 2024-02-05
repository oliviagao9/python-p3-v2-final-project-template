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
            return_main_menu_option()

        elif choice == "2":
            add_inventory()
            return_main_menu_option()

        elif choice == "3":
            view_current_inventory()
            update_inventory()
            return_main_menu_option()

        elif choice == "4":
            view_current_inventory()
            delete_inventory()
            return_main_menu_option()

        elif choice == "5":
            order_menu_option()

        elif choice == "6":
            exit_program()

        else:
            print("Please Enter a valid choice from 1 - 6")

def return_main_menu_option():
    time.sleep(1)
    print("If you want to go back to previous menu, please enter 1")
    print("If you want to exit the application, please enter 2")
    user_choice = input("> ")

    if user_choice == "1":
        time.sleep(0.5)
        main()

    elif user_choice == "2":
        exit_program()

def return_order_menu_option():
    time.sleep(1)
    print("If you want to go back to previous menu, please enter 1")
    print("If you want to exit the application, please enter 2")
    user_choice = input("> ")

    if user_choice == "1":
        time.sleep(0.5)
        order_menu_option()

    elif user_choice == "2":
        exit_program()

def order_menu_option():
    print("Please select an option for Order:")
    print("1. View Order List")
    print("2. Place an New Order")
    print("3. Edit an Existing Order")
    print("4. Delete Order")
    print("5. Exit")
    user_choice = input("> ")

    if user_choice == "1":
        view_current_inventory()
        return_order_menu_option()
    
    elif user_choice == "2":
        view_current_inventory()
        add_order()
        return_order_menu_option()

    elif user_choice == "3":
        view_current_order()
        time.sleep(0.3)
        print("Please enter the order id that you want to update")
        print("You can enter exit to go to other menu options")
        update_order()
        return_order_menu_option()
        
    elif user_choice == "4":
        view_current_order()
        delete_order()
        return_order_menu_option()
        
    elif user_choice == "5":
        exit_program()
        return_order_menu_option()

    else:
        print("Please Enter a valid choice from 1 - 5")
        order_menu_option()

if __name__ == "__main__":
    main()
