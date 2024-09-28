import bs4

class DateModule(Module):

    def __init__(self, name, dependencies=None):
        super().__init__(name, dependencies)

    def run(self):
        soup  = dependencies["html-parser"]
        soup.find_all("")