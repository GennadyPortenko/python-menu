from element import Element


class Menu:
    current_elem_index = 0

    def __init__(self, logger, elems_str=None):
        if elems_str is None:
            self.elements = [
                Element('empty')
            ]
        else:
            try:
                self.elements = eval(elems_str)
            except:
                self.elements = []
                for item in elems_str.split(';'):
                    if item and item.strip():
                        self.elements.append(Element(item.lstrip()))


        self.logger = logger
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
