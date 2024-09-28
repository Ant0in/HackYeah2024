
from reverse_helper import ReverseHelper
from bs4 import BeautifulSoup
import requests


class ReverseImg():

    def __init__(self, url: str) -> None:

        self.url: str = url

    def run(self, dependencies: list) -> dict:

        soup: BeautifulSoup = dependencies[0]['pages'][self.url]
        ...




if __name__ == '__main__':

    t = requests.get(url='https://padel-shop.pl/').text
    bs = BeautifulSoup(t, "html.parser")
