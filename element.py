class Element:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.selected = False

    def __repr__(self):
        return "Element({0}, {1})".format(self.name, self.value)

    def unselect(self):
        self.selected = False

    def select(self):
        self.selected = True
