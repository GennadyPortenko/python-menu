class Debug:
    def __init__(self, scr):
        self.scr = scr

    def log(self, line, text):
        self.scr.addstr(line, 0, text)
