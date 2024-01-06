from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "https://www.truecar.com/used-cars-for-sale/listings/audi/"

soup = BeautifulSoup(urlopen(URL), "html.parser")

cars_info = soup.find_all("div", {"class": "card-content order-3 vehicle-card-body"})

car_list = []
for car in cars_info:
    name = car.find("span", {"class": "truncate"}).text
    year = car.find("span", {"class": "vehicle-card-year text-xs"}).text
    operation = car.find("div", {"data-test": "vehicleMileage"}).text
    city = car.find("div", {"class": "vehicle-card-location mt-1 text-xs"}).text
    price = car.find("span", {"data-test": "vehicleListingPriceAmount"}).text
    car_list.append(name)
    car_list.append(year)
    car_list.append(operation)
    car_list.append(city)
    car_list.append(price)


print(car_list)
print(len(car_list))