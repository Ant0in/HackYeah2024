
from trustpilot_scrapper import TrustPilotScraper


class TrustPilotReviews:

    def __init__(self, dependencies: list[str], url: str) -> None:
        
        self.dependencies: list[str] = dependencies
        self.url: str = url

    def run(self) -> dict:
        return TrustPilotScraper.scrape_trustpilot(url=self.url)
    

if __name__ == '__main__':
    
    url = 'www.google.com'
    print(TrustPilotReviews(dependencies=..., url=url).run())