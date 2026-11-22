import random
from items import generate_loot


class Room:
    def __init__(self, room_type):
        self.room_type = room_type
        self.visited = False
        self.loot = []


class Maze:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.grid = {}
        self.generate_rooms()

    def generate_rooms(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[(x, y)] = Room("empty")

        coords = [(x, y) for x in range(self.width) for y in range(self.height)]
        random.shuffle(coords)

        key_pos = coords.pop()
        self.grid[key_pos] = Room("key")

        portal_pos = coords.pop()
        self.grid[portal_pos] = Room("portal")

        for _ in range(4):
            pos = coords.pop()
            self.grid[pos] = Room("chest")
            self.grid[pos].loot = generate_loot()

        for _ in range(3):
            pos = coords.pop()
            self.grid[pos] = Room("trap")

    def get_room(self, x, y):
        return self.grid.get((x, y))
