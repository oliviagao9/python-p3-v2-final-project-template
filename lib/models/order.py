from models.__init__ import CURSOR, CONN 

class Order:
    all = {}

    def __init__(self, product_id, name, price, quantity, order_number, order_dated):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.order_number = order_number
        self.order_dated = order_dated
    
    def __repr__(self):
      return f"[{self.id}: {self.product_id}, {self.name}, price: ${self.price}, quantity: {self.quantity}, 
        order_number: {self.order_number}, order_dated: {self.order_dated}]"