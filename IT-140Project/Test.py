from Room import Room
from Player import Player
room = Room('Entrance Hall')
player = Player()


def room_test():
    room.set_room(room.name)
    room.move("North")
    print(room.name)


def player_test():
    player.set_name(input('What is your name?'))
    print(player.name)
    room.set_room('Library')
    player.grab_item(room.item)
    print(player.inv)
    room.set_room('Kitchen')
    player.grab_item(room.item)
    print(player.inv)


room_test()
player_test()