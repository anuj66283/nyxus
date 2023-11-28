categories = ['electronics', 'clothes', 'cosmetic', 'grocery']

class InventoryItem:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def __str__(self):
        return f'Name: {self.name} Price: {self.price} Quantity: {self.quantity} Category: {self.category}'

class Electronics(InventoryItem):
    def __init__(self, name, price, quantity, category):
        super().__init__(self, name, price, quantity, category)

class InventoryManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def remove(self, item):
        for x in self.items:
            if x.name == item:
                self.items.remove(x)
                print("Removed")
                return
        print("Item not found")
    
    def update(self, item):
        for x in self.items:
            if x.name == item:
                price = int(input("Enter new price: "))
                quantity = int(input("Enter quantity: "))
                category = input("Enter category")

                x.price = price
                x.quantity = quantity
                x.category = category

                print("Update successful")
                return
        print("Item not found")
    
    def view(self, sort_order):

        if sort_order == 1:
            y = sorted(self.items, key=lambda x: x.name)
        elif sort_order == 2:
            y = sorted(self.items, key= lambda x: x.price)
        else:
            y = sorted(self.items, key = lambda x: x.quantity)

        for x in y:
            print(x)
        
    def lowstock(self):
        low = [x for x in self.items if x.quantity<10]

        if not low:
            print("All stocks are full")
            return
        print("Following items are low on stock")
        for x in low:
            print(f'Name: {x.name} Quantity: {x.quantity}')
                

def help():
    print("Here are available commands:\n\t1) add\n\t2) remove\n\t3) update\n\t4) view\n\t5) low stock")

help()

inv = InventoryManager()

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_name = input("Enter item name: ")

        try:
            price = int(input("Enter price: "))
            if price<0:
                print("Negative number not allowed")
                help()
                continue
        except:
            print("Please use integer")
            break

        try:
            quantity = int(input("ENter quantity"))
            if quantity<0:
                print("Negative number not allowed")
                help()
                continue
        except:
            print("Please use integer")
            help()
            continue
        
        category = input("Enter category: ")

        inv.add(InventoryItem(item_name, price, quantity, category))

    elif choice == 2:
        name = input("Enter item name")
        inv.remove(name)

    elif choice == 3:
        name = input("Enter item name")
        inv.update(name)
    
    elif choice == 4:
        resp = int(input("How do you want to sort? (1) name\n2) price\n3)) quantity"))

        if resp<1 or resp>3:
            print("Invalid input")
            continue

        inv.view(resp)

    elif choice == 5:
        inv.lowstock()
    
    elif choice == 6:
        help()
    
    else:
        break