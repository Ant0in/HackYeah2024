import bs4
import whois

class DateModule(Module):

    def __init__(self, name, dependencies=None):
        super().__init__(name, dependencies)

    def run(self):
        w = self.dependencies["whois"]
        return w["creation_date"]