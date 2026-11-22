import random

class Item:
    def __init__(self, name, item_type, weight, value):
        self.name = name
        self.item_type = item_type
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"{self.name} (вес: {self.weight}, цена: {self.value})"


def generate_loot():
    possible_items = [
        Item("Зелье лечения", "potion", 0.5, 10),
        Item("Ржавый меч", "weapon", 3.0, 5),
        Item("Золотая монета", "gold", 0.1, 50),
        Item("Старый щит", "armor", 5.0, 15),
        Item("Факел", "misc", 1.0, 2),
    ]
    count = random.randint(1, 3)
    return [random.choice(possible_items) for _ in range(count)]


def generate_starting_inventory():
    return [Item("Зелье лечения", "potion", 0.5, 10) for _ in range(2)]
