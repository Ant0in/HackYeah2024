import requests
from bs4 import BeautifulSoup
import json
import time

scam_list = []

for i in range(1, 20):
    req = requests.get(f"https://www.watchlist-internet.at/liste-betruegerischer-shops/?tx_solr%5Bpage%5D={i}")
    soup = BeautifulSoup(req.text, features="html.parser")
    table = soup.select_one(selector="#news-section-pagination > div.filter-section > div.js-filter-panel > div:nth-child(3)")

    links = soup.select(selector=".site-item__link")

    for site in links:
        scam_list.append(site.text.strip())

    time.sleep(1)

    print("page", i, "done")

with open("sample_dataset.json", "w") as f:
    json.dump(scam_list, f)
    

