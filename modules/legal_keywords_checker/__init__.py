
from modules.legal_keywords_checker.legal import LegalChecker


class LegalKeywordsChecker:

    def __init__(self, url: str) -> None:
        self.url: str = url

    def run(self, dependencies: list | None = None) -> dict:
        return LegalChecker.extract_info(url=self.url)
    

