from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "https://www.truecar.com/used-cars-for-sale/listings/audi/"

soup = BeautifulSoup(urlopen(URL), "html.parser")

print(soup.text)