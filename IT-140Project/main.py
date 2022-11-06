from Room import Room
from Player import Player
room = Room('Entrance Hall')
player = Player()


def main():
    fin = False
    print('\"You are a rogue adventurer searching an abandoned castle for any valuables to sell.')
    print('The barkeep at the local tavern said it was probably full of valuables since nobody dared to go near it'
          ' because of a local legend.')
    print('The legend states that a necromancer took residence in the castle many years ago '
          'and that anyone who ventured near would be used in his experiments.')
    print('You, not fearing a local superstition, decided this could be a chance to fill your pockets.\"\n')
    player.set_name(input('First off, What is your name?\n'))
    room.set_room(room.name)
    while not fin:
        player_input = input('What do you want to do?\n')
        if player_input == 'I':
            player.grab_item(room.item)
        else:
            room.move(player_input)
            print(room.name)


if __name__ == "__main__":
    main()
