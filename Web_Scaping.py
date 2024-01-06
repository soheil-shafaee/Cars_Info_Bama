from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conx = pymysql.connect(host="localhost",
                       user="root",
                       password="",
                       database="cars_information")

cur = conx.cursor()

for n in range(1, 5):
    URL = f"https://www.truecar.com/used-cars-for-sale/listings/audi/?page={n}"

    soup = BeautifulSoup(urlopen(URL), "html.parser")

    cars_info = soup.find_all("div", {"class": "card-content order-3 vehicle-card-body"})

    car_list = []
    for car in cars_info:
        name = car.find("span", {"class": "truncate"}).text
        year = int(car.find("span", {"class": "vehicle-card-year text-xs"}).text)
        operation = car.find("div", {"data-test": "vehicleMileage"}).text.split()[0].split(",")
        int_operation = int("".join(operation))
        city = car.find("div", {"class": "vehicle-card-location mt-1 text-xs"}).text
        price = car.find("span", {"data-test": "vehicleListingPriceAmount"}).text.split("$")[1].split(",")
        int_price = int("".join(price))
        sql = (name, year, int_operation, city, int_price)
        com = """
        INSERT INTO cars_info
        VALUES(%s, %i, %i, %s, %i)
        """ % sql

        try:
            cur.execute(com)
            conx.commit()

        except Exception as e:
            print(e)
            conx.rollback()

        conx.close()

