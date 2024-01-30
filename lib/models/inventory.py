from models.__init__ import CURSOR, CONN 

class Inventory:

    all = {}

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

    def save(self):
        sql = """
            INSERT INTO inventories (name, price, quantity)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.price, self.quantity))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, price, quantity):
        inventory = cls(name, price, quantity)
        inventory.save()
        return inventory
    
    def update(self):
        sql = """
            UPDATE inventories
            SET name = ?, price = ?, quantity = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.quantity))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM inventories
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        name = self.name
        del type(self).all[self.id]

        self.id = None

        print(f'Inventory {name} is deleted')

    @classmethod
    def instance_from_db(cls, row):

        inventory = cls.all.get(row[0])
        if inventory:
            inventory.name = row[1]
            inventory.price = row[2]
            inventory.quantity = row[3]
        else:
            inventory = cls(row[1], row[2], row[3])
            inventory.id = row[0]
            cls.all[inventory.id] = inventory
        return inventory
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM inventories
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM inventories
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM inventories
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None