from models.__init__ import CURSOR, CONN 

class Inventory:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"[{self.id}: {self.name}, price: ${self.price}, quantity: {self.quantity}]"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self._price = price
        else:
            print("Please enter a valid price for inventory")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS inventories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER,
            quantity INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS inventories;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, price, quantity):
        inventory = cls(name, price, quantity)
        sql = """
            INSERT INTO inventories (name, price, quantity)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (inventory.name, inventory.price, inventory.quantity))
        CONN.commit()

        inventory.id = CURSOR.lastrowid

        return inventory