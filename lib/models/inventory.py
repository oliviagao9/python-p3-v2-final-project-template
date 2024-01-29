from models.__init__ import CURSOR, CONN 

class Inventory:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"[{self.id}: {self.name}, price: ${self.price}, quantity: {self.quantity}]"

