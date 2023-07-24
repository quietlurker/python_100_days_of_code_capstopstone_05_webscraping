from bs4 import BeautifulSoup
import requests


class ZillowOffers:
    def __init__(self, zillow_url):
        self.url = zillow_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept-Language": "pl,en-US;q=0.7,en;q=0.3"
        }
        self.prices = []
        self.addresses = []
        self.links = []

    def get_listings(self):
        r = requests.get(url=self.url, headers=self.headers)
        ramen = BeautifulSoup(r.text, "html.parser")

        list_of_offers = ramen.select(selector="div .property-card-data")
        for item in list_of_offers:
            self.addresses.append(item.find("a").text)
            # format links if https://www.zillow.com/ misssing
            raw_link = item.find("a")['href']
            if "https://www.zillow.com/" not in raw_link:
                link = "https://www.zillow.com/" + raw_link
                self.links.append(link)
            else:
                self.links.append(raw_link)
            # format prices '$2,837+ 1 bd' ->2,837
            raw_price = item.find("span", {"data-test": "property-card-price"}).text
            price = int(raw_price.replace("/", "+").split("+")[0][1:].replace(",",""))
            self.prices.append(price)



