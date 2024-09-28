
import requests
from bs4 import BeautifulSoup


class LegalChecker:

    @staticmethod
    def check_https(url):
        return url.startswith("https://")
    
    @staticmethod
    def checkLegalKeywords(soup) -> bool:
        legal_terms_keywords = ['cgv', 'return policy', 'refund policy']
        page_text = soup.get_text().lower()
        cgv_present = any(keyword in page_text for keyword in legal_terms_keywords)
        return cgv_present
    
    @staticmethod
    def extract_info(url):

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
        except:
            return None
        cgv_present = LegalChecker.checkLegalKeywords(soup=soup)
        return {
            "HTTPS": LegalChecker.check_https(url),
            "CGV - return/refund policy": cgv_present,
        }
    

if __name__ == "__main__":
    url = 'https://www.dolcevitashoessouthafrica.com/'
    print(LegalChecker.extract_info(url=url))