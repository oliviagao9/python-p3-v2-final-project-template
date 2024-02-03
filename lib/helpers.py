# lib/helpers.py
from models.inventory import Inventory

def exit_program():
    print("Goodbye!")
    exit()

def view_current_inventory(nameOnly=None):

    inventory_items = Inventory.get_all()
    if nameOnly:
        for item in inventory_items:
            print(f"Product Id: {item.id} | Product Name: {item.name}")
    else :
        for item in inventory_items:
            print(f"Product Id: {item.id} | Product Name: {item.name} | Price: {item.price} | Quantity: {item.quantity}")

def update_inventory():
    pass