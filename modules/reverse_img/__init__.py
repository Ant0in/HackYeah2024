# from modules import Module
from bs4 import BeautifulSoup


class ReverseImg():
    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies or []

    def run(self):
        soup: BeautifulSoup = self.dependencies[0]

        for img in soup.find_all("img"):
            href = img.get("src")
            if href is not None:
                print(href)


if __name__ == "__main__":
    soup = BeautifulSoup("<img src=\"test.com\" /><img src=\"test1.com\" />", features="html.parser")
    module = ReverseImg("Test", [soup])

    module.run()
