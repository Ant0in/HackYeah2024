import whois

class WhoisLookupModule(Module):
    def __init__(self, name, dependencies=None):
        super().__init__(name, dependencies)

    def run(self):
        # Fetch WHOIS data from the DNS
        w = whois.whois(self.dependencies["url"])
        return w