class Manager(object):

    def __init__(self, menu):
        self.menu = menu
        

    def next(self):
        self.menu.__dispatch__("next")