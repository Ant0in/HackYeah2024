

import requests
import re


class MediaModule:

    def __init__(self, url: str) -> None:
        self.url = url

    def run(self, dependencies: list | None = None) -> object:

        soup = dependencies[0]['pages'][self.url]
        keywords = ["instagram", "facebook", "twitter"]
        links = []

        for a_tag in soup.find_all('a'):
            for attr in a_tag.attrs:
                if any(keyword in str(a_tag.attrs[attr]).lower() for keyword in keywords):
                    links.append(a_tag.get('href'))
                    break


        regexes = [
            r"(https:\/\/)?(www\.)?instagram\.com\/[A-Za-z0-9_.]+\/?", 
            r"(https:\/\/)?(www\.)?facebook\.com\/[A-Za-z0-9_.]+\/?", 
            r"(https:\/\/)?(www\.)?twitter\.com\/[A-Za-z0-9_.]+\/?"
        ]
        
        for link in links:
            if not any(re.fullmatch(regex, link.strip()) for regex in regexes):
                return {'score': 0}
        
        if links: return {'score': 1}
        else: dict()