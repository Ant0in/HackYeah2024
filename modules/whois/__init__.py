
import whois


class WhoisLookupModule:
    
    def __init__(self, url: str) -> None:
        self.url: str = url

    def run(self) -> ...:
        # Fetch WHOIS data from the DNS
        w = whois.whois(self.url)
        return w