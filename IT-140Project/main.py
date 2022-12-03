from Room import Room
from Player import Player
room = Room('')
player = Player()


def game_loop():
    fin = False  # variable to check if the game is fin
    room.set_room('Entrance Hall')  # set starting room as Entrance Hall
    while not fin:
        print('----------------')
        print('Location: {}'.format(room.name)) # print current room
        print('Inventory: {}'.format(player.inv))
        print('----------------')
        # print the games controls.
        print('Tip: Press \'I\' to examine the room closer. You may find something of value.')
        if 'Map' in player.inv:
            print('Tip: Press \'M\' to use the map.')
        print('Tip: Use the \'WASD\' keys to move through doorways.')
        print('Enter \'EXIT\' to end the game.')
        player_input = str.upper(input('What do you want to do?\n'))  # receive players input and format it to uppercase
        if player_input == 'EXIT': # check for exit statement
            break
        if player_input == 'I': # Collect item
            player.grab_item(room.item)
        elif player_input == 'M': # View map
            room.use_map()
        else: # Move rooms. exceptions are handled in the move function.
            room.move(player_input)
        if room.name == 'King\'s Chamber':
            fin = True
            if len(player.inv) == 8:  # if player has all items print winning statement
                print('You enter the King\'s Chamber. You see a silhouette in-front of you')
                print('This figure appears to be the source of the chanting.'
                      ' You draw the Holy Golden Sword as you approach.')
                print('The Necromancer turns to face you, his green eyes shining through the fog.')
                print('It\'s a tough battle, but using the Spell Book you are able to negate his spells')
                print('and the Blessed Sword allows you to defeat the Necromancer.')
                print('After you defeat him you see that he was performing a ritual or some sort. '
                      'There is a note nearby.\n')
                player.grab_item(room.item)
            # if the player is missing items, print a losing statement explaining why the player lost
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
                print('This figure appears to be the source of the chanting. '
                      'You draw the Holy Golden Sword as you approach.')
                print('The Necromancer turns to face you, his green eyes shining through the fog.')
                print('You attempt to fight him, but you can feel your strength fading as his grows.')
                print('If you had a way to block his spells you could land a killing blow, '
                      'but eventually you lose the fight.\n')
    # check if the player wants to end the game or try again
    try_again = input('Do you want to try again? \"Y\" for Yes or \"N\" for No.\n')
    if try_again == 'Y':
        room.set_room('Entrance Hall')
        game_loop()


def main():
    # Print storyboard
    print('\"You are a rogue adventurer searching an abandoned castle for any valuables to sell.')
    print('The barkeep at the local tavern said it was probably full of valuables since nobody dared to go near it')
    print('because of a local legend.')
    print('The legend states that a necromancer took residence in the castle many years ago ')
    print('and that anyone who ventured near would be used in his experiments.')
    print('You, not fearing a local superstition, decided this could be a chance to fill your pockets.\"\n')
    # run game_loop function
    game_loop()
    # print thank you after game loop ends
    print('Thank you for playing!')


if __name__ == "__main__":
    main()
