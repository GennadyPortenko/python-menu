from curses import wrapper
from arguments import Arguments
from socketlogger import SocketLogger

from menu import Menu
from curses_view import View

DEBUG = True

CLIP_CMD_WINDOWS = 'clip'
CLIP_CMD_LINUX = 'xclip -sel clip'
CLIP_CMD = CLIP_CMD_LINUX

ENTER_KEY = '\n'

args = Arguments().args
logger = SocketLogger(args.logging_port)


def main(stdscr):
    menu = Menu(logger, args.delimiter, args.items)
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

    while True:
        view.refresh()
        c = stdscr.getkey()
        # logger.log(f'Pressed : {c}')
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
