import requests
import re

class MediaModule:
    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies

    def run(self):
        url = self.dependencies["url"]
        soup = self.dependencies["HTMLParser"][url]

        keywords = ["instagram", "facebook", "twitter"]
        links = []

        for a_tag in soup.find_all('a'):
            for attr in a_tag.attrs:
                if any(keyword in str(a_tag.attrs[attr]).lower() for keyword in keywords):
                    links.append(a_tag.get('href'))
                    break


        regexes = ["(https?:\/\/)?(www\.)?instagram\.com\/[A-Za-z0-9_.]+\/?", "(https?:\/\/)?(www\.)?facebook\.com\/[A-Za-z0-9_.]+\/?", "(https?:\/\/)?(www\.)?twitter\.com\/[A-Za-z0-9_.]+\/?"]
        for link in links:
            if not any(re.match(regex, link) for regex in regexes):
                return 0
            
        return 1