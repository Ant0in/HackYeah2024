

from bs4 import BeautifulSoup
import requests
from reverse_image_search import GoogleReverseImageSearch



class ReverseHelper:
    
    @staticmethod
    def get_images_link(url: str, soup: BeautifulSoup) -> list[str]:

        images = soup.find_all('img')
        ret: list[str] = list()

        for img in images:
            img_src = img.get('src')
            if img_src:
                img_url = requests.compat.urljoin(url, img_src)
                print(img_url)
                ret.append(img_url)
        
        return ret
    
    @staticmethod
    def reverse_search(imurl: str) -> None:
        request = GoogleReverseImageSearch()

        response = request.response(
            query="test",
            image_url=imurl,
            max_results=5
        )

        print(response)





#url: str = 'https://pl.aliexpress.com/?src=google&albch=fbrnd&acnt=304-410-9721&isdl=y&aff_short_key=UneMJZVf&albcp=21416161801&albag=165497748364&slnk=&trgt=kwd-14802285088&plac=&crea=703760166711&netw=g&device=c&mtctp=e&memo1=&albbt=Google_7_fbrnd&aff_platform=google&albagn=888888&isSmbActive=false&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjw0t63BhAUEiwA5xP54b3CnLvz8BNNxVDukMSSxObA_s2j1rA1EPf9icx2l040LsOHEpJ5XxoCk9EQAvD_BwE&gatewayAdapt=glo2pol'
#t = requests.get(url=url).text
#bs = BeautifulSoup(t, "html.parser")
ReverseHelper.reverse_search("https://ae-pic-a1.aliexpress-media.com/kf/Sd3c9f959d78242f5b0f165f129d1c57d1.jpg_480x480.jpg_.webp")