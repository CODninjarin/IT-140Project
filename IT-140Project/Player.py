from Room import Room


class Player:
    def __init__(self):
        self.name = ''
        self.inv = []

    def grab_item(self, item):
        if item not in self.inv:
            self.inv.append(str(item))
            print('{} has collected the {}'.format(self.name, item))
        else:
            print('You have already collected the {}'.format(item))

    def set_name(self, new_name):
        self.name = new_name
