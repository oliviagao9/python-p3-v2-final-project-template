from models.inventory import Inventory
from models.order import Order

Inventory.drop_table()
Inventory.create_table()

Inventory.create("Red Rose", 3.50, 2)
Inventory.create("Sunflower Large", 3.00, 10)
Inventory.create("Rosemary", 2.0 , 5)
Inventory.create("Baby's Breath", 2.00, 10)
Inventory.create("Calla Lilies", 2.00, 10)
Inventory.create("Forget Me Not", 3.00, 10)
Inventory.create("Tulips", 2.00, 10)
Inventory.create("Iris", 1.5, 15)
Inventory.create("Pink Rose", 2, 15)
Inventory.create("Ti Leaf", 2, 15)

Order.drop_table()
Order.create_table()

Order.create("Red Rose", 10, 1)
Order.create("Iris", 5, 7)
Order.create("Rosemary", 3, 3)