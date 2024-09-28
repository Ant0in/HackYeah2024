
from modules.trustpilot_checker.trustpilot_scrapper import TrustPilotScraper


class TrustPilotReviews:

    def __init__(self, url: str) -> None:
        self.url: str = url

    def run(self, dependencies: list[str]) -> dict:
        return TrustPilotScraper.scrape_trustpilot(url=self.url)
    

if __name__ == '__main__':
    
    url = 'http://google.com'
    print(TrustPilotReviews(dependencies=..., url=url).run())