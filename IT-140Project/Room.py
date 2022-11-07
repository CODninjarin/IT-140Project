class Room:
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.item = ''
        self.directions = ['w', 'W', 'a', 'A', 's', 'S', 'd', 'D']
        self.map = []

    def set_room(self, name):
        # Entrance Hall
        if name == 'Entrance Hall':
            self.name = name
            self.exits = ['North']
            self.item = 'Map'
            print('You have entered the castle\'s Entrance Hall.')
            print('There is a doorway to the North.')
            if name not in self.map:
                print('There appears to be a piece of paper near the next doorway, it may be something helpful.')
        # Entrance Hallway
        if name == 'Entrance Hallway':
            self.name = name
            self.exits = ['North', 'South', 'East', 'West']
            self.item = ''
            print('You entered the Entrance Hallway. There are doors in all 4 directions, but the East and North')
            print('appear to be blocked be debris.')
        # Library
        if name == 'Library':
            self.name = name
            self.exits = ['North', 'West']
            self.item = 'Spell Book'
            print('You have entered the Library. Everything looks like it hasn\'t been touched in years except for')
            print('a few Spell Books laying open on a table. There are doorways to the North and East')
            if name not in self.map:
                print('One of those Spell Books might come in handy and if not, you could always sell it!')
        # Kitchen
        if name == 'Kitchen':
            self.name = name
            self.exits = ['South', 'West']
            self.item = 'Potions'
            print('You have entered the Kitchen. Several alchemical ingredients are laying on the counters as')
            print('well as some Potions. There are doorways to the East and South.')
            if name not in self.map:
                print('Those Potions might come in handy if you run into whoever made them.')
        # Great Hall
        if name == 'Great Hall':
            self.name = name
            self.exits = ['North', 'South', 'East', 'West']
            self.item = 'Adventurer\'s Note'
            print('You have entered the Great Hall. Near the throne you see a long dead adventurer')
            if name not in self.map:
                print('That adventurer may have something that can help you. He certainly won\'t be needing it back.')
        # Armory
        if name == 'Armory':
            self.name = name
            self.exits = ['South', 'East']
            self.item = 'Leather Armor'
            print('You have entered the Armory. There are sets of heavy metal armor in various places.')
            print('There are doorways to the West and South.')
            if name not in self.map:
                print('If you look around you might find something lighter you could use.')
        # Weapon Stash
        if name == 'Weapon Stash':
            self.name = name
            self.exits = ['North', 'East']
            self.item = 'Blessed Golden Sword'
            print('You have entered the Weapon Stash. There are swords, shields, and bows laying all around.')
            print('There is a doorway to the West that appears to be blocked with debris and a doorway to the North')
            if name not in self.map:
                print('There appears to be a faint glow behind a pile of swords.')
        # Bedroom Hallway
        if name == 'Bedroom Hallway':
            self.name = 'Bedroom Hallway'
            self.exits = ['North', 'South', 'East', 'West']
            self.item = ''
            print('You have entered the Bedroom Hallway. Thick fog fills the air and a green glow appears to be coming')
            print('from the doorway to the North. A faint chanting can be heard from the other side of the door.')
            print('There are doorways in a 4 directions. You should probably check all the rooms before going through')
            print('the North door.')
        # Bedroom
        if name == 'Bedroom':
            self.name = name
            self.exits = ['West']
            self.item = 'Gold Cups'
            print('You have entered a Bedroom. It looks like hasn\'t been cleaned in years.')
            print('There is a doorway to the East')
            if name not in self.map:
                print('There may be some valuables hidden in the dust.')
        # Queen's Chamber
        if name == 'Queen\'s Chamber':
            self.name = name
            self.exits = ['East']
            self.item = 'Fine Jewelry'
            print('You have entered the Queen\'s Chamber. The room looks pristine as if the castle was never abandoned.')
            print('There is a doorway to the West')
            if name not in self.map:
                print('You see something sparkling near the dresser.')
        # Kings Chamber
        if name == 'King\'s Chamber':
            self.name = name
            self.exits = ['South']
            self.item = 'Necromancer\'s Note'
        print('\nTip: Press \'I\' to examine the room closer. You may find something of value.')
        print('Tip: Use the \'WASD\' keys to move through doorway.\n')
        self.map.append(name)

    def move(self, direction):
        valid_direction = False
        if direction in self.directions:
            if direction == 'w' or direction == 'W':
                direction = 'North'
                valid_direction = True
            elif direction == 'a' or direction == 'A':
                direction = 'West'
                valid_direction = True
            elif direction == 's' or direction == 'S':
                direction = 'South'
                valid_direction = True
            elif direction == 'd' or direction == 'D':
                direction = 'East'
                valid_direction = True
        else:
            print('Invalid Entry')
        if direction in self.exits:
            if self.name == 'Entrance Hall':
                if direction == 'North':
                    self.set_room('Entrance Hallway')
            elif self.name == 'Entrance Hallway':
                if direction == 'North' or direction == 'West':
                    print('This way is blocked.')
                elif direction == 'East':
                    self.set_room('Library')
                elif direction == 'South':
                    self.set_room('Entrance Hall')
            elif self.name == 'Library':
                if direction == 'North':
                    self.set_room('Kitchen')
                if direction == 'West':
                    self.set_room('Entrance Hallway')
            elif self.name == 'Kitchen':
                if direction == 'West':
                    self.set_room('Great Hall')
                if direction == 'South':
                    self.set_room('Library')
            elif self.name == 'Great Hall':
                if direction == 'West':
                    self.set_room('Armory')
                if direction == 'South':
                    self.set_room('This way is blocked.')
                if direction == 'East':
                    self.set_room('Kitchen')
                if direction == 'North':
                    self.set_room('Bedroom Hallway')
            elif self.name == 'Armory':
                if direction == 'East':
                    self.set_room('Great Hall')
                elif direction == 'South':
                    self.set_room('Weapon Stash')
            elif self.name == 'Weapon Stash':
                if direction == 'East':
                    self.set_room('This way is blocked')
                elif direction == 'North':
                    self.set_room('Armory')
            elif self.name == 'Bedroom Hallway':
                if direction == 'East':
                    self.set_room('Bedroom')
                elif direction == 'West':
                    self.set_room('Queen\'s Chamber')
                elif direction == 'South':
                    self.set_room('Great Hall')
                elif direction == 'North':
                    self.set_room('King\'s Chamber')
            elif self.name == 'Bedroom':
                if direction == 'West':
                    self.set_room('Bedroom Hallway')
            elif self.name == 'Queen\'s Chamber':
                if direction == 'East':
                    self.set_room('Bedroom Hallway')
        else:
            if valid_direction:
                print('There is no doorway in that direction.')

    def set_name(self, new_name):
        self.name = new_name

    # use the map to see the names of the rooms attached to the current room.
    def use_map(self):
        if self.name == 'Entrance Hall':
            print('The Entrance Hallway is to the North.')
