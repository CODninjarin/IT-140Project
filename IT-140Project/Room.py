class Room:
    # class variable assignments
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.item = ''
        self.directions = ['W', 'A', 'S', 'D']
        self.map = []

    # Function used to set the current room.
    # Has one argument, name, which is the name of the room the user is setting.
    def set_room(self, name):
        # Entrance Hall
        # Has an exit to the North(Entrance Hall)
        # Has the "Map" item
        if name == 'Entrance Hall':
            self.name = name
            self.exits = ['North']
            self.item = 'Map'
            print('You have entered the castle\'s Entrance Hall.')
            print('There is a doorway to the North.')
            # Nested statement to check if the player has entered the room. This is in every statement.
            if name not in self.map:
                print('There appears to be a piece of paper near the next doorway, it may be something helpful.')
        # Entrance Hallway
        # Has four exits West(Library), South(Entrance Hall), and the North and East are blocked.
        # Has no item due to it being a hallway.
        if name == 'Entrance Hallway':
            self.name = name
            self.exits = ['North', 'South', 'East', 'West']
            self.item = ''
            print('You entered the Entrance Hallway. There are doors in all 4 directions, but the East and North')
            print('appear to be blocked be debris.')
        # Library
        # Has two exits, North(Kitchen) and East(Entrance Hall)
        # Has one item, "Spell Book"
        if name == 'Library':
            self.name = name
            self.exits = ['North', 'West']
            self.item = 'Spell Book'
            print('You have entered the Library. Everything looks like it hasn\'t been touched in years except for')
            print('a few Spell Books laying open on a table. There are doorways to the North and East')
            if name not in self.map:
                print('One of those Spell Books might come in handy and if not, you could always sell it!')
        # Kitchen
        # Has two exits, East(Great Hall) and South(Library)
        # Has one item, "Potions"
        if name == 'Kitchen':
            self.name = name
            self.exits = ['South', 'West']
            self.item = 'Potions'
            print('You have entered the Kitchen. Several alchemical ingredients are laying on the counters as')
            print('well as some Potions. There are doorways to the East and South.')
            if name not in self.map:
                print('Those Potions might come in handy if you run into whoever made them.')
        # Great Hall
        # Has four exits, East(Armory), North(Great Hallway)
        if name == 'Great Hall':
            self.name = name
            self.exits = ['North', 'South', 'East', 'West']
            self.item = 'Adventurer\'s Note'
            print('You have entered the Great Hall. Near the throne you see a long dead adventurer')
            if name not in self.map:
                print('That adventurer may have something that can help you. He certainly won\'t be needing it back.')
        # Armory
        # Has two doors, South(Weapon Stash) and East(Great Hall)
        # Has the "Leather Armor" item
        if name == 'Armory':
            self.name = name
            self.exits = ['South', 'East']
            self.item = 'Leather Armor'
            print('You have entered the Armory. There are sets of heavy metal armor in various places.')
            print('There are doorways to the West and South.')
            if name not in self.map:
                print('If you look around you might find something lighter you could use.')
        # Weapon Stash
        # Has two doors, North(Armory) and one to the East that is blocked.
        # Has the "Holy Golden Sword" item
        if name == 'Weapon Stash':
            self.name = name
            self.exits = ['North', 'East']
            self.item = 'Blessed Golden Sword'
            print('You have entered the Weapon Stash. There are swords, shields, and bows laying all around.')
            print('There is a doorway to the West that appears to be blocked with debris and a doorway to the North')
            if name not in self.map:
                print('There appears to be a faint glow behind a pile of swords.')
        # Bedroom Hallway
        # Has four doors, North(King's Chamber), East(Bedroom), West(Queen's Chamber), and South(Great Hall)
        # Has no item due to being a hallway
        if name == 'Bedroom Hallway':
            self.name = 'Bedroom Hallway'
            self.exits = ['North', 'South', 'East', 'West']
            self.item = ''
            print('You have entered the Bedroom Hallway. Thick fog fills the air and a green glow appears to be coming')
            print('from the doorway to the North. A faint chanting can be heard from the other side of the door.')
            print('There are doorways in a 4 directions. You should probably check all the rooms before going through')
            print('the North door.')
        # Bedroom
        # Has one door, West(Bedroom Hallway)
        # Has the "Gold Cups" item
        if name == 'Bedroom':
            self.name = name
            self.exits = ['West']
            self.item = 'Gold Cups'
            print('You have entered a Bedroom. It looks like hasn\'t been cleaned in years.')
            print('There is a doorway to the East')
            if name not in self.map:
                print('There may be some valuables hidden in the dust.')
        # Queen's Chamber
        # Has one door, East(Bedroom Hallway)
        # Has the "Fine Jewelry" item
        if name == 'Queen\'s Chamber':
            self.name = name
            self.exits = ['East']
            self.item = 'Fine Jewelry'
            print('You have entered the Queen\'s Chamber. The room looks pristine as if the castle was never abandoned.')
            print('There is a doorway to the West')
            if name not in self.map:
                print('You see something sparkling near the dresser.')
        # Kings Chamber
        # Has one door, South(Bedroom Hallway). This is not used in the game at this time.
        # Has the "Necromancer's Note" item that the player obtains by winning the game
        if name == 'King\'s Chamber':
            self.name = name
            self.exits = ['South']
            self.item = 'Necromancer\'s Note'
        self.map.append(name)

    # function to move the player to a new room
    def move(self, direction):
        valid_direction = False  # variable to check if direction is a valid direction
        # check if direction is one of the four directions and change it to the compass direction
        # also sets valid_direction to true if the direction is valid
        if direction in self.directions:
            if direction == 'W':
                direction = 'North'
                valid_direction = True
            elif direction == 'A':
                direction = 'West'
                valid_direction = True
            elif direction == 'S':
                direction = 'South'
                valid_direction = True
            elif direction == 'D':
                direction = 'East'
                valid_direction = True
        else:  # print statement for if direction is not a valid direction
            print('Invalid Entry')
            # check if direction in the current rooms exits and set the new room if it is
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
            if valid_direction:  # if direction is valid, but not an exit, print no doorway in direction
                print('There is no doorway to the {}.'.format(direction))

    # use the map to see the names of the rooms attached to the current room.
    def use_map(self):
        print('\n')
        if self.name == 'Entrance Hall':
            print('The Entrance Hallway is to the North.')
        if self.name == 'Entrance Hallway':
            print('The Library is to the East.')
            print('The Entrance Hall is to the south.')
            print('The Weapons Stash is to the West, but it is blocked by debris.')
            print('the Great Hall is to the North, but it is blocked by debris.')
        if self.name == 'Library':
            print('The Kitchen is to the North.')
            print('The Entrance Hallway is to the West.')
        if self.name == 'Kitchen':
            print('The Great Hall is to the West.')
            print('The Library is to the South')
        if self.name == 'Great Hall':
            print('The Kitchen is to the East.')
            print('The Entrance Hallway is to the south.')
            print('The Armory is to the West.')
            print('the Bedroom Hallway is to the North.')
        if self.name == 'Armory':
            print('The Great Hall is to the East.')
            print('The Weapon Stash is to the South')
        if self.name == 'Weapon Stash':
            print('The Armory is to the North.')
            print('The Entrance Hallway is to the East')
        if self.name == 'Bedroom Hallway':
            print('The Queen\'s Chamber is to the West.')
            print('The Great Hall is to the South')
            print('The Bedroom is to the East.')
            print('The King\'s Chamber is to the North')
        if self.name == 'Bedroom':
            print('The Bedroom Hallway is to the West.')
        if self.name == 'Queen\'s Chamber':
            print('The Bedroom Hallway is to the East.')
        if self.name == 'King\'s Chamber':
            print('The Bedroom Hallway is to the South')
        print('\n')

