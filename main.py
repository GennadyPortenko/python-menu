from curses import wrapper
import os
from curses_debug import Debug

from menu import Menu
from curses_view import View

from argparse import ArgumentParser

CLIP_CMD_WINDOWS = 'clip'
CLIP_CMD_LINUX = 'xclip -sel clip'
CLIP_CMD = CLIP_CMD_LINUX

ENTER_KEY = '\n'

parser = ArgumentParser()
parser.add_argument('--menu')
args = parser.parse_args()


def main(stdscr):
    debug = Debug(stdscr)

    menu = Menu(debug, args.menu)
    view = View(menu, stdscr)

    actions = {
        'KEY_DOWN': lambda: menu.down(),
        'KEY_UP': lambda: menu.up(),
        'j': lambda: menu.down(),
        'k': lambda: menu.up(),

        # Enter
        # ENTER_KEY: lambda: os.system('echo ' + menu.current_element().value.strip() + '| ' + CLIP_CMD)
        ENTER_KEY: lambda: ()
    }

    stdscr.clear()

    c = None
    while True:
        view.refresh()
        c = stdscr.getkey()
        if c == 'q' or c == ENTER_KEY:
            view.exit()
            break
        if actions.get(c) is not None:
            actions.get(c)()

    if actions.get(c) is not None:
        actions.get(c)()
    exit(menu.current_elem_index)


if __name__ == '__main__':
    wrapper(main)
