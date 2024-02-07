from helpers import *
import time

def greeting():
    logo = '''
    _____ _                      __        __               ____            _                 
    |  ___| | _____      _____ _ _\ \      / /_ _ _ __ ___  / ___| _   _ ___| |_ ___ _ __ ___  
    | |_  | |/ _ \ \ /\ / / _ \ '__\ \ /\ / / _` | '__/ _ \ \___ \| | | / __| __/ _ \ '_ ` _ \ 
    |  _| | | (_) \ V  V /  __/ |   \ V  V / (_| | | |  __/  ___) | |_| \__ \ ||  __/ | | | | |
    |_|   |_|\___/ \_/\_/ \___|_|    \_/\_/ \__,_|_|  \___| |____/ \__, |___/\__\___|_| |_| |_|
                                                                |___/                          
    '''
    print(logo)
    time.sleep(0.5)
    print("Hi There, Welcome to FlowerWare Inventory Management System")
    time.sleep(0.5)

def main():
    greeting()
    while True:
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
            view_current_inventory(True)
            delete_inventory()
            return_main_menu_option()

        elif choice == "5":
            order_menu_option()

        elif choice == "6":
            exit_program()

        else:
            print("Please Enter a valid choice from 1 - 6")
            
def menu():
    print("Please Select an Option From Menu Below:")
    print("1. View Current Inventory")
    print("2. Add Inventory")
    print("3. Update Inventory Quantity")
    print("4. Delete Inventory")
    print("5. Place Order")
    print("6. Exit")

def update_inventory_menu():
    print("Please select an option:")
    print("1. Edit Current Inventory Quantity")
    print("2. Add New Inventory")
    print("3. Delete Inventory")
    print("4. Exit")

def return_main_menu_option():
    time.sleep(1)
    print("If you want to go back to previous menu, please enter 1")
    print("If you want to exit the application, please enter 2")
    user_choice = input("> ")

    if user_choice == "1":
        time.sleep(0.5)

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
    time.sleep(0.5)
    print("Please select an option for Order:")
    print("1. View Order List")
    print("2. Place an New Order")
    print("3. Edit an Existing Order")
    print("4. Delete Order")
    print("5. Exit")
    user_choice = input("> ")

    if user_choice == "1":
        view_current_order()
        return_order_menu_option()
    
    elif user_choice == "2":
        view_current_inventory()
        add_order()
        return_order_menu_option()

    elif user_choice == "3":
        view_current_order(True)
        time.sleep(0.3)
        print("Please enter the order id that you want to update")
        print("You can enter exit to go to other menu options")
        update_order()
        return_order_menu_option()
        
    elif user_choice == "4":
        view_current_order(True)
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
