
from legal import LegalChecker


class LegalKeywordsChecker:

    def __init__(self, dependencies: list[str], url: str) -> None:
        
        self.dependencies: list[str] = dependencies
        self.url: str = url

    def run(self) -> dict:
        return LegalChecker.extract_info(url=self.url)
    

if __name__ == '__main__':
    
    url = 'https://www.dolcevitashoessouthafrica.com'
    print(LegalKeywordsChecker(dependencies=..., url=url).run())