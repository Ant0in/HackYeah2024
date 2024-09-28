import whois

class WhoisLookupModule:
    def __init__(self, name, dependencies=None):
        self.name = name
        self.dependencies = dependencies

    def run(self):
        # Fetch WHOIS data from the DNS
        w = whois.whois(self.dependencies["url"])
        return w