from models.inventory import Inventory
from models.order import Order
import time

def exit_program():
    print("Goodbye!")
    exit()

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

                if product_to_delete.orders():
                    for order in product_to_delete.orders():
                        Order.delete((order))

                Inventory.delete(product_to_delete)
                print(f"{inventory_to_delete} is succesfully deleted from inventory")
                break
            else:
                print("The product name you entered is not found, please enter a correct product name")
                print("You can enter exit to go to menu options")

def view_current_order(show_id = None):
    order_items = Order.get_all()
    if show_id:
        for item in order_items:
            print(f" Order Number {item.id} | Product Name: {item.name} | Product Id: {item.product_id}| Quantity: {item.quantity}")
    else :
        for index, item in enumerate (order_items):
            print(f" {index + 1} | Product Name: {item.name} | Product Id: {item.product_id}| Quantity: {item.quantity}")

def add_order():
    while True:
        print("Please enter a product name you want to order")
        
        while True:
            product_name = input("> ")

            if isinstance(product_name, str) and len(product_name):
                if not Inventory.find_by_name(product_name):
                    print("This product name is not found, please enter a correct product name.")
                    time.sleep(0.3)
                    continue

                product_id = Inventory.find_by_name(product_name).id
                print(f"Please enter the quantity of {product_name} you want to order")

                while True:
                    product_quantity = input(">")
                    try:
                        int(product_quantity)
                        break
                    except Exception: 
                        print("Please enter whole number for the product quantity")
                
                try:
                    Order.create(product_name, int(product_quantity), product_id)
                    break
                except Exception as exc:
                    print(exc)
                
        print("The order is successfully placed!")
        time.sleep(0.3)
        break 

def update_order():
    print("Please Enter The Order Number That You Want to Update")
    while True:
        order_number = input("> ")
        if order_number == "exit":
            break
        else: 
            try:
                int(order_number)
                if int(order_number) and not Order.find_by_id(int(order_number)):
                    print("Order is not found, please enter a correct order id")
                    continue
                order = Order.find_by_id(int(order_number))
                order_id = order_number
                order_product_name = order.name

            except Exception: 
                print("Please Enter a Correct Order ID")
                continue
            
            print("Please enter a new quantity that you want to update")
            while True:
                order_new_quantity = input("> ")
                try:
                    int(order_new_quantity)
                    break
                except Exception: 
                    print("Please enter whole number for new order quantity")
            
            Order.update_quantity(order_id, int(order_new_quantity))
            time.sleep(0.3)
            print(f"Order Number {order_number}, {order_product_name}'s quantity is updated to {order_new_quantity}")
            time.sleep(0.3)
            break

def delete_order():
    time.sleep(0.3)
    print("Please enter the Order Number that you want to delete")
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
                    print(f"Order number {choice} is succesfully deleted from inventory")
                    break

                print("Order is not found, please enter a correct order number")

            except Exception: 
                print("Please Enter a Correct Order Number")
    
        break

def show_order_by_inventory():
    print("Please enter a product name to check on orders")
    while True:
        choice = input("> ")

        if Inventory.find_by_name(choice):
            inventory = Inventory.find_by_name(choice)
            if inventory.orders():
                print('-------------------------------------------------------------------------------------------------------')
                for order in inventory.orders():
                    print(f'Order Number {order.id} | Product Name: {order.name} | Product Id: {order.product_id}| Quantity: {order.quantity}')
                print('-------------------------------------------------------------------------------------------------------')

                time.sleep(0.5)
                break
            else:
                print('-------------------------------------------------------------------------------------------------------')
                print(f'There is currently no orders placed on {inventory.name}, please enter another product name or type exit to show other menu options')
                print('-------------------------------------------------------------------------------------------------------')

        elif choice == 'exit':
            break