class Element:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.selected = False

    def unselect(self):
        self.selected = False

    def select(self):
        self.selected = True
