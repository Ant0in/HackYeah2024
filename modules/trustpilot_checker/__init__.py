
from modules.trustpilot_checker.trustpilot_scrapper import TrustPilotScraper


class TrustPilotReviews:

    def __init__(self, url: str) -> None:
        self.url: str = url

    def run(self, dependencies: list | None = None) -> dict:
        return TrustPilotScraper.scrape_trustpilot(url=self.url)
    