from Room import Room
from Player import Player
room = Room('Entrance Hall')
player = Player()


def game_loop():
    fin = False
    while not fin:
        print('\nLocation: {}'.format(room.name))
        player_input = input('What do you want to do?\n')
        if player_input == 'I':
            player.grab_item(room.item)
        else:
            room.move(player_input)
        if room.name == 'King\'s Chamber':
            fin = True
    if len(player.inv) == 8:
        print('You enter the King\'s Chamber. You see a silhouette in-front of you')
        print('This figure appears to be the source of the chanting. You draw the Holy Golden Sword as you approach.')
        print('The Necromancer turns to face you, his green eyes shining through the fog.')
        print('It\'s a tough battle, but using the Spell Book you are able to negate his spells')
        print('and the Blessed Sword allows you to defeat the Necromancer.')
        print('After you defeat him you see that he was performing a ritual or some sort. There is a note nearby.\n')
        player.grab_item(room.item)
    elif 'Blessed Golden Sword' not in player.inv and 'Spell Book' not in player.inv \
            and 'Adventurer\'s Note' not in player.inv:
        print('You enter the King\'s Chamber. You see a silhouette in-front of you')
        print('This figure appears to be the source of the chanting. You draw your Dagger as you approach.')
        print('The Necromancer turns to face you, his green eyes shining through the fog.')
        print('You attempt to fight him, but you can feel your strength fading as his grows.\n')
        print('Some better equipment may have saved your life.')
    elif 'Blessed Golden Sword' not in player.inv and 'Spell Book' not in player.inv:
        print('You enter the King\'s Chamber. You see a silhouette in-front of you')
        print('This figure appears to be the source of the chanting. You draw your Dagger as you approach.')
        print('The Necromancer turns to face you, his green eyes shining through the fog.')
        print('You attempt to fight him, but you can feel your strength fading as his grows.')
        print('You should have looked for the Blessed Sword and a way to counter his Spells.\n')
    elif 'Blessed Golden Sword' not in player.inv:
        print('You enter the King\'s Chamber. You see a silhouette in-front of you')
        print('This figure appears to be the source of the chanting. You draw your Dagger as you approach.')
        print('The Necromancer turns to face you, his green eyes shining through the fog.')
        print('You attempt to fight him, but without the Blessed Sword you can\'t land a finishing blow.')
        print('Even with the aid of the Spell Book it\'s not enough to protect you from your fate\n')
    elif 'Spell Book' not in player.inv:
        print('You enter the King\'s Chamber. You see a silhouette in-front of you')
        print('This figure appears to be the source of the chanting. You draw the Holy Golden Sword as you approach.')
        print('The Necromancer turns to face you, his green eyes shining through the fog.')
        print('You attempt to fight him, but you can feel your strength fading as his grows.')
        print('If you had a way to block his spells you could land a killing blow, but eventually you lose the fight.\n')
        try_again = input('Do you want to try again? \"Y\" for Yes or \"N\" for No.')
        if try_again == 'Y':
            game_loop()


def main():
    print('\"You are a rogue adventurer searching an abandoned castle for any valuables to sell.')
    print('The barkeep at the local tavern said it was probably full of valuables since nobody dared to go near it')
    print('because of a local legend.')
    print('The legend states that a necromancer took residence in the castle many years ago ')
    print('and that anyone who ventured near would be used in his experiments.')
    print('You, not fearing a local superstition, decided this could be a chance to fill your pockets.\"\n')
    room.set_room(room.name)
    game_loop()


if __name__ == "__main__":
    main()
