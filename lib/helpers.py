# lib/helpers.py
from models.inventory import Inventory
from models.order import Order
from cli import *
import time

def exit_program():
    print("Goodbye!")
    exit()

def menu():
    print("Please select an option:")
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

def view_current_inventory(nameOnly=None):

    inventory_items = Inventory.get_all()
    if nameOnly:
        for item in inventory_items:
            print(f"Product Id: {item.id} | Product Name: {item.name}")
    else :
        for item in inventory_items:
            print(f"Product Id: {item.id} | Product Name: {item.name} | Price: {item.price} | Quantity: {item.quantity}")

def add_inventory():
    while True:
        print("Please enter the product name")
        product_name = input("> ")
        while True:
            if isinstance(product_name, str) and len(product_name):
                if Inventory.find_by_name(product_name):
                    print("This product name is already taken, please enter a different one.")
                    time.sleep(0.3)
                    add_inventory()

                print("Please enter the price of the product")
                while True:
                    product_price = input(">")
                    try:
                        float(product_price)
                        product_price = float(product_price)
                        break
                    except Exception as exc: 
                        print("Please enter integer for product price")
                        continue

                print("Please enter the quantity of the product")
                while True:
                    product_quantity = input(">")
                    try:
                        int(product_quantity)
                        break
                    except Exception as exc: 
                        print("Please enter whole number for product quantity")
                        continue
                
            try:
                Inventory.create(product_name, product_price, product_quantity)
                break
            except Exception as exc:
                print(exc)
        print("The new inventory is successfully added!")
        time.sleep(0.3)
        break 
        
def update_inventory():
    time.sleep(0.3)
    print("Please enter the product name that you want to update the quantity")
    print("You can enter exit to go to other menu options")
    while True:
        choice = input("> ")

        if choice == "exit":
            break
        else: 
            if (Inventory.find_by_name(choice)):
                print("Please enter the new quantity")
                while True:
                    quantity_choice = input(">")
                    try:
                        int(quantity_choice)
                        break
                    except Exception as exc: 
                        print("Please enter whole number for product quantity")
                        continue
                    
                Inventory.update_quantity(Inventory.find_by_name(choice).id, int(quantity_choice))
                print(f"{choice}'s quantity is updated to {quantity_choice}")
                break
            else:
                print("The product name you entered is not found, please enter a correct product name")
                print("You can enter exit to go to menu options")
        
def delete_inventory():
    time.sleep(0.3)
    print("Please enter the product name that you want to delete from inventory")
    print("You can enter exit to go to other menu options")
    while True:
        choice = input("> ")

        if choice == "exit":
            break
        else: 
            if (Inventory.find_by_name(choice)):
                Inventory.delete(Inventory.find_by_name(choice))
                print(f"{choice} is succesfully deleted from inventory")
                break
            else:
                print("The product name you entered is not found, please enter a correct product name")
                print("You can enter exit to go to menu options")

def add_order():
    while True:
        print("Please enter a product name you want to order")
        product_name = input("> ")
        while True:
            if isinstance(product_name, str) and len(product_name):
                if not Inventory.find_by_name(product_name):
                    print("This product name is not found, please enter a correct product name.")
                    time.sleep(0.3)
                    add_order()

                product_id = Inventory.find_by_name(product_name).id
                print(f"Please enter the quantity of {product_name} you want to order")
                while True:
                    product_quantity = input(">")
                    try:
                        int(product_quantity)
                        break
                    except Exception as exc: 
                        print("Please enter whole number for product quantity")
                        continue
                
            try:
                Order.create(product_name, int(product_quantity), product_id)
                break
            except Exception as exc:
                print(exc)
        print("The order is successfully placed!")
        time.sleep(0.3)
        break 