class Player:
    def __init__(self,name):
        self.name = name
        self.inventory = [] # empty list for inventory

    def add_to_inventory(self,item): # adding to inventory
        self.inventory.append(item)

    def show_inventory(self): # displaying inventory 
        print("Inventory:")
        for item in self.inventory:
            print("-", item) # displaying "-" with item 
