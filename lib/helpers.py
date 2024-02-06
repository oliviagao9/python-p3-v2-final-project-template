from models.inventory import Inventory
from models.order import Order
import time

def exit_program():
    print("Goodbye!")
    exit()

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

def view_current_inventory(nameOnly=None):

    inventory_items = Inventory.get_all()
    if nameOnly:
        for item in inventory_items:
            print(f"Product Name: {item.name}")
    else :
        for item in inventory_items:
            print(f"Product Name: {item.name} | Price: {item.price} | Quantity: {item.quantity}")

def add_inventory():
    while True:
        print("Please enter the product name")
        while True:

            while True:
                product_name = input("> ")

                try:
                    int(product_name) 
                    print("Please Enter String Data Type for The Product Name")
                    continue
                except Exception:
                    if isinstance(product_name, str) and len(product_name):
                        if Inventory.find_by_name(product_name):
                            print("This product name is already taken, please enter a different one.")
                            time.sleep(0.3)
                            continue
                        else:
                            break

            print("Please enter the price of the product")
            while True:
                product_price = input(">")
                try:
                    float(product_price)
                    product_price = float(product_price)
                    break
                except Exception: 
                    print("Please enter integer for product price")

            print("Please enter the quantity of the product")
            while True:
                product_quantity = input(">")
                try:
                    int(product_quantity)
                    break
                except Exception: 
                    print("Please enter whole number for product quantity")
                
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
        update_choice = input("> ")

        if update_choice == "exit":
            break
        else: 
            if (Inventory.find_by_name(update_choice)):
                product = Inventory.find_by_name(update_choice)
                print("Please enter the new quantity")

                while True:
                    new_quantity = input(">")
                    try:
                        int(new_quantity)
                        product_id = product.id
                        break
                    except Exception: 
                        print("Please enter whole number for product quantity")
                    
                Inventory.update_quantity(product_id, int(new_quantity))
                print(f"{update_choice}'s quantity is updated to {new_quantity}")
                break
            else:
                print("The product name you entered is not found, please enter a correct product name")
                print("You can enter exit to go to other menu options")
        
def delete_inventory():
    time.sleep(0.3)
    print("Please enter the product name that you want to delete from inventory")
    print("You can enter exit to go to other menu options")

    while True:
        inventory_to_delete = input("> ")

        if inventory_to_delete == "exit":
            break
        else: 
            if (Inventory.find_by_name(inventory_to_delete)):
                product_to_delete = Inventory.find_by_name(inventory_to_delete)
                Inventory.delete(product_to_delete)
                print(f"{inventory_to_delete} is succesfully deleted from inventory")
                break
            else:
                print("The product name you entered is not found, please enter a correct product name")
                print("You can enter exit to go to menu options")

def add_order():
    while True:
        print("Please enter a product name you want to order")
        new_product = input("> ")
        
        while True:
            if isinstance(new_product, str) and len(new_product):
                if not Inventory.find_by_name(new_product):
                    print("This product name is not found, please enter a correct product name.")
                    time.sleep(0.3)
                    continue

                product_id = Inventory.find_by_name(new_product).id
                print(f"Please enter the quantity of {new_product} you want to order")

                while True:
                    product_quantity = input(">")
                    try:
                        int(product_quantity)
                        break
                    except Exception: 
                        print("Please enter whole number for product quantity")
                
                try:
                    Order.create(new_product, int(product_quantity), product_id)
                    break
                except Exception as exc:
                    print(exc)
                
        print("The order is successfully placed!")
        time.sleep(0.3)
        break 

def view_current_order(show_id = None):

    order_items = Order.get_all()
    if show_id:
        for item in range (order_items):
            print(f" Order Id{item.id} | Product Name: {item.name} | Product Id: {item.product_id}| Quantity: {item.quantity}")
    else :
        for index, item in enumerate (order_items):
            print(f" {index + 1} | Product Name: {item.name} | Product Id: {item.product_id}| Quantity: {item.quantity}")


def update_order():
    while True:
        choice = input("> ")

        if choice == "exit":
            break
        else: 
            while True:
                try:
                    int(choice)
                    if int(choice) and Order.find_by_id(int(choice)):
                        order_id = Order.find_by_id(int(choice)).id
                        break

                    print("Order is not found, please enter a correct order id")
                    update_order()

                except Exception as exc: 
                    print("Please Enter a Correct Order ID")
                    update_order()
            
            print("Please enter correct number for product quantity")
            while True:
                order_new_quantity = input("> ")
                try:
                    int(order_new_quantity)
                    break
                except Exception as exc: 
                    print("Please enter whole number for new order quantity")
            
            Order.update_quantity(order_id, int(order_new_quantity))
            time.sleep(0.3)
            print(f"Order Id {choice}'s quantity is updated to {order_new_quantity}")
            break

def delete_order():
    time.sleep(0.3)
    print("Please enter the order id that you want to delete")
    print("You can enter exit to go to other menu options")
    while True:
        choice = input("> ")

        if choice == "exit":
            break
        else: 
            try:
                int(choice)
                if int(choice) and Order.find_by_id(int(choice)):
                    order = Order.find_by_id(int(choice))
                    Order.delete(order)
                    print(f"{choice} is succesfully deleted from inventory")
                    break

                print("Order is not found, please enter a correct order id")

            except Exception: 
                print("Please Enter a Correct Order ID")
    
        break