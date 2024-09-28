import requests
from bs4 import BeautifulSoup

class HTMLParserModule:

    def __init__(self, url: str) -> None:
        
        self.url: str = url
        
    def run(self, dependencies: list | None = None):

        pages_dict = {self.url: self.parse_page(self.url)}
        for link in pages_dict[self.url].find_all("a", href=True):

            # If link starts with the base url then adds it to the dict
            if str(link["href"]).startswith(self.url):
                pages_dict[link["href"]] = self.parse_page(link["href"])

            # If link is relative
            if str(link["href"]).startswith("/"):
                absolute_link = self.url + link["href"][1:]
                pages_dict[absolute_link] = self.parse_page(absolute_link)

            if len(pages_dict) >= 10:
                break

        return {'pages': pages_dict}

    def get_text(self, url):
        r = requests.get(url)
        return r.text
    
    def parse_page(self, url):
        text = self.get_text(url)
        soup = BeautifulSoup(text, "html.parser")
        return soup