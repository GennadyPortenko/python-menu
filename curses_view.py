import curses
from enum import IntEnum, auto


class View:
    def __init__(self, menu, scr):
        self.menu = menu
        self.scr = scr

        curses.init_pair(self.Colors.SELECTED, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(self.Colors.UNSELECTED, curses.COLOR_WHITE, curses.COLOR_BLACK)

    class Colors(IntEnum):
        SELECTED = auto()
        UNSELECTED = auto()

    def print_line(self, n, text, color):
        self.scr.addstr(n, 0, text, curses.color_pair(color))

    def refresh(self):
        for i, element in enumerate(self.menu.elements):
            color = self.Colors.SELECTED if element.selected else self.Colors.UNSELECTED
            self.print_line(i, element.name, color)
        self.scr.refresh()
