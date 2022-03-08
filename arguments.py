from argparse import ArgumentParser

class Arguments:
    def __init__(self, ):
        parser = ArgumentParser()
        parser.add_argument('--items')
        parser.add_argument('--delimiter')
        parser.add_argument('--element-inner-separator')
        parser.add_argument('--logging-port')
        self.args = parser.parse_args()