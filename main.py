from curses import wrapper
import os
from curses_debug import Debug

from menu import Menu
from curses_view import View

stop = False


def stop_loop():
    stop = True


def main(stdscr):
    debug = Debug(stdscr)

    menu = Menu(debug)
    view = View(menu, stdscr)

    stop = False

    actions = {
        'KEY_DOWN': lambda: menu.down(),
        'KEY_UP': lambda: menu.up(),
        # Enter
        '\n': lambda: os.system('echo ' + menu.current_element().value.strip() + '| clip')
    }

    stdscr.clear()

    while not stop:
        view.refresh()
        c = stdscr.getkey()
        if c == 'q':
            break
        action = actions.get(c)
        if action is not None:
            action()


if __name__ == '__main__':
    wrapper(main)
