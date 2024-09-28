
from trustpilot_scrapper import TrustPilotScraper


class TrustPilotReviews:

    def __init__(self, name: str, dependencies: list[str], url: str) -> None:
        
        self.name: str = name
        self.dependencies: list[str] = dependencies
        self.url: str = url

    def run(self) -> dict:
        return TrustPilotScraper.scrape_trustpilot(url=self.url)
    

if __name__ == '__main__':
    
    url: str = 'one-time-offer.com'
    print(TrustPilotReviews(name='TrustPilotReviews', dependencies=..., url=url).run())