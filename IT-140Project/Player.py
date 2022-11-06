from Room import Room


class Player:
    def __init__(self):
        self.name = ''
        self.inv = []

    def grab_item(self, item):
        self.inv.append(str(item))

    def set_name(self, new_name):
        self.name = new_name