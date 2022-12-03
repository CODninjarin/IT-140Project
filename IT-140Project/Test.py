from Room import Room
from Player import Player

room = Room('Entrance Hall')
player = Player()


def test():
    # Entrance Hall, Map
    print(room.name)
    room.set_room(room.name)
    player.grab_item(room.item)
    room.move("W")
    # Entrance Hallway, Nothing
    print(room.name)
    room.move("D")
    player.grab_item(room.item)
    # Library, Spell Book
    print(room.name)
    room.move("W")
    player.grab_item(room.item)
    # Kitchen, Potions
    print(room.name)
    room.move("A")
    player.grab_item(room.item)
    # Great Hall, Adventurer's Note
    print(room.name)
    room.move("A")
    player.grab_item(room.item)
    # Armory, Leather Armor
    print(room.name)
    room.move("S")
    player.grab_item(room.item)
    # Weapons Stash, Holy Golden Sword
    print(room.name)
    room.move("W")
    player.grab_item(room.item)
    # Armory, Already collected
    print(room.name)
    room.move("D")
    player.grab_item(room.item)
    # Great Hall, Already collected
    print(room.name)
    room.move("W")
    player.grab_item(room.item)
    # Bedroom Hallway, Nothing
    print(room.name)
    room.move("D")
    player.grab_item(room.item)
    # Bedroom, Gold Cup
    print(room.name)
    room.move("A")
    player.grab_item(room.item)
    # Bedroom Hallway, Nothing
    print(room.name)
    room.move("A")
    player.grab_item(room.item)
    # Queen's Chamber, Fine Jewelry
    print(room.name)
    room.move("D")
    player.grab_item(room.item)
    # Bedroom Hallway, Nothing
    print(room.name)
    room.move("W")
    player.grab_item(room.item)
    # King's Chamber
    print(room.name)
    print(player.inv)
    # Invalid entry test
    room.move('test')
    # No doorway test
    room.move('A')


test()

