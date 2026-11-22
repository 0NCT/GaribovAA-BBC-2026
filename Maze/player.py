class Player:
    def __init__(self, x, y):
        self.hp = 100
        self.max_hp = 100
        self.x = x
        self.y = y
        self.inventory = []
        self.has_key = False

    def add_item(self, item):
        self.inventory.append(item)  # append

    def add_multiple_items(self, items):
        self.inventory.extend(items)  # extend

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)  # remove

    def drop_last_item(self):
        if self.inventory:
            return self.inventory.pop()  # pop
        return None

    def sort_inventory(self, by="value"):
        if by == "value":
            self.inventory.sort(key=lambda item: item.value)  # sort
        elif by == "weight":
            self.inventory.sort(key=lambda item: item.weight)

    def reverse_inventory(self):
        self.inventory.reverse()  # reverse

    def find_item_index(self, item_name):
        names = [item.name for item in self.inventory]
        if item_name in names:  # in
            return names.index(item_name)  # index
        return -1

    def copy_inventory(self):
        return self.inventory.copy()  # copy

    def get_inventory_slice(self, start, end):
        return self.inventory[start:end]  # slice

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
