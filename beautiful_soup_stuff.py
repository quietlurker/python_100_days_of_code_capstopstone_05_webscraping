from bs4 import BeautifulSoup
import requests


class ZillowOffers:
    def __init__(self):
        self.url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.88646946005285%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.66394700757486%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
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
            # format prices '$2,837+ 1 bd' ->2,837
            raw_price = item.find("span", {"data-test": "property-card-price"}).text
            price = int(raw_price.replace("/", "+").split("+")[0][1:].replace(",",""))
            self.prices.append(price)



