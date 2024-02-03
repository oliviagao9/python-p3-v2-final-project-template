# lib/cli.py

from helpers import *

def greeting():
    print("Hi there welcome to Olivia Florist Inventory Management System")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            view_inventory()
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            place_order()
        elif choice == "4":
            exit()
        else:
            print("Please Enter a valid choice from 1 - 4")


def menu():
    print("Please select an option:")
    print("1. View Current Inventory")
    print("2. Update Inventory")
    print("3. Place Order")
    print("4. Exit")

if __name__ == "__main__":
    main()
