import requests
from bs4 import BeautifulSoup

class HTMLParserModule:

    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies
    
    
    def run(self):
        base_url = self.dependencies["url"]
        pages_dict = {base_url: self.parse_page(base_url)}
        for link in pages_dict[base_url].find_all("a", href=True):

            # If link starts with the base url then adds it to the dict
            if str(link["href"]).startswith(base_url):
                pages_dict[link["href"]] = self.parse_page(link["href"])

            # If link is relative
            if str(link["href"]).startswith("/"):
                absolute_link = base_url + link["href"][1:]
                pages_dict[absolute_link] = self.parse_page(absolute_link)

            if len(pages_dict) >= 10:
                break

        return pages_dict

    def get_text(self, url):
        r = requests.get(url)
        return r.text
    
    def parse_page(self, url):
        text = self.get_text(url)
        soup = BeautifulSoup(text, "html.parser")
        return soup