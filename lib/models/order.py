from models.__init__ import CURSOR, CONN 
from models.inventory import Inventory

class Order:
    all = {}

    def __init__(self, name, quantity, product_id, id =None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.product_id = product_id
        # self.order_number = order_number
        # self.order_dated = order_dated
    
    def __repr__(self):
      return f"[{self.id}: {self.product_id}, {self.name}]"
    
    # quantity: {self.quantity}, 
    #     order_number: {self.order_number}, order_dated: {self.order_dated}

    @property
    def name(self):
       return self._name
    
    @name.setter
    def name(self, name):
      if isinstance(name, str) and len(name):
        # if Inventory.find_by_name(name):
          self._name = name 
        # else:
        #     raise ValueError ("product name must reference a department in the database")
      else: 
        raise ValueError("Name must be a non-empty string")
    
    @property
    def quantity(self):
       return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
      if type(quantity) is int:
        self._quantity = quantity
      else:
         raise ValueError("quantity must be an integer")

    @property
    def product_id(self):
       return self._product_id
    
    @product_id.setter
    def product_id(self, product_id):
      if type(product_id) is int and Inventory.find_by_id(product_id):
        self._product_id = product_id
      else:
         raise ValueError("product_id must reference a product in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER,
            product_id INTEGER,
            FOREIGN KEY (product_id) REFERENCES inventories(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS orders;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
                INSERT INTO orders (name, quantity, product_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.quantity, self.product_id))
        CONN.commit()
        breakpoint()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def update_quantity(cls, order_id, quantity):
        old_order_quantity = Order.find_by_id(order_id).quantity
        sql = """
            UPDATE orders
            SET quantity = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (quantity, order_id))
        CONN.commit()

        product_id = Order.find_by_id(order_id).product_id

        original_quantity = Inventory.find_by_id(product_id).quantity
        new_inventory_quantity = original_quantity - old_order_quantity + quantity
        Inventory.update_quantity(product_id, new_inventory_quantity)

       
    @classmethod
    def create(cls, name, quantity, product_id):
        order = cls(name, quantity, product_id)
        order.save()

        original_quantity = Inventory.find_by_id(product_id).quantity
        Inventory.update_quantity(product_id, quantity + original_quantity)
        return order
    
    @classmethod
    def instance_from_db(cls, row):

        # Check the dictionary for  existing instance using the row's primary key
        order = cls.all.get(row[0])
        if order:
            # ensure attributes match row values in case local instance was modified
            order.name = row[1]
            order.quantity = row[2]
            order.product_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            order = cls(row[1], row[2], row[3])
            order.id = row[0]
            cls.all[order.id] = order
        return order
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM orders
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM orders
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None