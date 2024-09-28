import bs4
import whois

class UpdateDateModule(Module):

    def __init__(self, name, dependencies=None):
        super().__init__(name, dependencies)

    def run(self):
        w = self.dependencies["whois"]
        return w["update_date"]