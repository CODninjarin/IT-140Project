class Player:
    def __init__(self):
        self.inv = []

    def grab_item(self, item):
        if item != '':  # check if there is an item in the room or not
            if item not in self.inv:  # check if the item is already in the players inventory
                # if no, add to inventory and print description
                self.inv.append(str(item))
                print('You have collected the {}'.format(item))
                self.item_desc(item)
            else:
                # if yes, print that player has already collected it
                print('You have already collected the {}'.format(item))
        else:
            # if there is no item, print a statement saying there is no item
            print('There doesn\'t appear to be anything of interest.')

    # function describing each item in the game
    def item_desc(self, item):
        if item == 'Map':
            print('It\'s a map of the castle, this will come in handy.')
        if item == 'Spell Book':
            print('This book is filled with magic spells, you read through the pages')
        if item == 'Potions':
            print('These Health and Stamina potions should come in handy.')
        if item == 'Adventurer\'s Note':
            print('The note says: \"If you found this note I must be dead.')
            print('I didn\'t the believe stories about this place, but they appear to be true.')
            print('The Necromancer uses dark magic attack that draw your life force away.')
            print('The only way I could think to defeat him is with a sword blessed by light. There may be something')
            print('in the Weapon Stash, but I don\'t think i\'ll make it there to find out.\"')
            if 'Spell Book' in self.inv:
                print('The spells the note mentions appear to be in the Spell Book, maybe you can learn to '
                      'defend against them.')
            if 'Holy Golden Sword' in self.inv:
                print('Good thing you got that Sword earlier, you might not get out of here without it.')
        if item == 'Leather Armor':
            print('This armor is much finer than your current armor. It may not provide much protection,'
                  'but it\'s easier to move around in than those sets of metal armor.')
        if item == 'Blessed Golden Sword':
            print('The sword has a faint golden glow and feels warm to the touch.')
            if 'Adventurer\'s Note' in self.inv:
                print('This must be the Sword the Adventurer\'s Note mentioned.'
                      'Maybe with this I can stop that Necromancer.')
        if item == 'Gold Cups':
            print('These are definitely worth something.')
        if item == 'Fine Jewelry':
            print('If you make it out of here with these you could buy a castle of your own!')
        if item == 'Necromancer\'s Note':
            print('The note says: \"I don\'t know what else I can do. I cannot live without you '
                  'my dear wife. My Queen. I will bring you back to me.\"')

    # function to print the players inventory
    def show_inv(self):
        print('Inventory: {}'.format(self.inv))
