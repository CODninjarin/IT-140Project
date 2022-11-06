
class Room:
    def __init__(self,name):
        self.name = name
        self.exits = []
        self.item = ''
        self.directions = ['w', 'W', 'a', 'A', 's', 'S', 'd', 'D']

    def set_room(self, name):
        if name == 'Entrance Hall':
            self.name = name
            self.exits = ['North']
            self.item = 'Map'
            print('You have entered the castle\'s Entrance Hall. There is a doorway to the North.')
            print('Tip: Press \'I\' to examine the room closer. You may find something of value.')
            print('Tip: Use the \'WASD\' keys to move through doorways.')
        if name == 'Entrance Hallway':
            self.name = name
            self.exits = ['North', 'South', 'East', 'West']
            self.item = ''
        if name == 'Library':
            self.name = name
            self.exits = ['North', 'East']
            self.item = 'Spell Book'
        if name == 'Kitchen':
            self.name = name
            self.exits = ['South', 'East']
            self.item = 'Potion'
        if name == 'Great Hall':
            self.name = name
            self.exits = ['North', 'South', 'East', 'West']
            self.item = 'Adventurer\'s Note'
        if name == 'Armory':
            self.name = name
            self.exits = ['South', 'West']
            self.item = 'Leather Armor'
        if name == 'Weapon Stash':
            self.name = name
            self.exits = ['North', 'West']
            self.item = 'Blessed Golden Sword'
        if self.name == 'Bedroom Hallway':
            self.name = name
            self.exits = ['North', 'South', 'East', 'West']
            self.item = ''
        if name == 'Bedroom':
            self.name = name
            self.exits = ['East']
            self.item = 'Gold Cup'
        if name == 'Queen\'s Chambers':
            self.name = name
            self.exits = ['West']
            self.item = 'Fine Jewelry'
        if name == 'King\'s Chambers':
            self.name = name
            self.exits = ['South']
            self.item = ''

    def move(self, direction):
        if direction in self.directions:
            if direction == 'w' or 'W':
                direction = 'North'
            elif direction == 'a' or 'A':
                direction = 'East'
            elif direction == 's' or 'S':
                direction = 'South'
            elif direction == 'd' or 'D':
                direction = 'West'
            if direction in self.exits:
                if self.name == 'Entrance Hall':
                    if direction == 'North':
                        self.set_room('Entrance Hallway')
                elif self.name == 'Entrance Hallway':
                    if direction == "North" or "East":
                        print('This way is blocked.')
                    if direction == "West":
                        self.set_room('Library')
                    if direction == "South":
                        self.set_room('Entrance Hall')
                elif self.name == 'Library':
                    if direction == "North":
                        self.set_room('Kitchen')
                    if direction == 'East':
                        self.set_room('Entrance Hallway')
                elif self.name == 'Kitchen':
                    if direction == 'East':
                        self.set_room('Great Hall')
                    if direction == 'South':
                        self.set_room('Library')
                elif self.name == 'Great Hall':
                    if direction == 'East':
                        self.set_room('Armory')
                    if direction == 'South':
                        self.set_room('Library')
                    if direction == 'East':
                        self.set_room('Great Hall')
                    if direction == 'South' or '':
                        self.set_room('Library')
                elif self.name == 'Entrance Hall':
                    self.set_room('Entrance Hallway')
                elif self.name == 'Entrance Hall':
                    self.set_room('Entrance Hall')
                elif self.name == 'Entrance Hall':
                    self.set_room('Entrance Hallway')
                elif self.name == 'Entrance Hall':
                    self.set_room('Entrance Hallway')
        else:
            print('Invalid Entry')

    def set_name(self, new_name):
        self.name = new_name
