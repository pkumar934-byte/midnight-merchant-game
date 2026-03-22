class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Inventory:
    def __init__(self):
        self.items = [
            Item("Basic Sword", "A weak iron sword.", 10),
            Item("Basic Sword", "A weak iron sword.", 10),
            Item("Basic Sword", "A weak iron sword.", 10),
            Item("Magic Wand", "Shoots sparks.", 25),
            Item("Health Potion", "Restores some hp.", 15)
        ]

    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
