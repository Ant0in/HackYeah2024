
import whois


class WhoisLookupModule:
    
    """
    Gather WhoIS data using Whois lib. Does not provide any score.
    """
    
    def __init__(self, url: str) -> None:
        self.url: str = url

    def run(self, dependencies: list = None) -> ...:
        # Fetch WHOIS data from the DNS
        w = whois.whois(self.url)
        return w