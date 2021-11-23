from element import Element


class Menu:
    elements = (
        Element('connect to host', "ssh user@somehost"),
        Element('build', "mvn install")
    )
    current_elem_index = 0

    def __init__(self, debug):
        self.debug = debug
        self.elements[self.current_elem_index].select()

    def is_last_elem(self):
        return self.current_elem_index == len(self.elements) - 1

    def is_first_elem(self):
        return self.current_elem_index == 0

    def current_element(self):
        return self.elements[self.current_elem_index]

    def down(self):
        if self.is_last_elem():
            next_index = 0
        else:
            next_index = self.current_elem_index + 1
        self.elements[self.current_elem_index].unselect()
        self.elements[next_index].select()
        self.current_elem_index = next_index

    def up(self):
        if self.is_first_elem():
            next_index = len(self.elements)-1
        else:
            next_index = self.current_elem_index - 1
        self.elements[self.current_elem_index].unselect()
        self.elements[next_index].select()
        self.current_elem_index = next_index
