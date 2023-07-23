from beautiful_soup_stuff import ZillowOffers
# google form link:
google_form = "https://docs.google.com/forms/d/e/1FAIpQLSc3d7bBiq3xuWwLQGaiok9pY5dB85VDtm5kvtYQ5kauIe_kFg/viewform?usp=sf_link"

offers = ZillowOffers()

offers.get_listings()
print(offers.addresses)
print(offers.links)
print(offers.prices)





