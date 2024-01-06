import pymysql

conx = pymysql.connect(host="localhost",
                       user="root",
                       password="",
                       database="cars_information"
                       )

cur = conx.cursor()

com = """CREATE TABLE cars_info(
    Car_Name VARCHAR(30),
    Model INT(4),
    Operation INT,
    City VARCHAR(30),
    Price INT,
    PRIMARY KEY (Car_Name, Model)
)
"""

try:
    cur.execute(com)
    conx.commit()

except Exception as e:
    print(e)
    conx.rollback()

conx.close()
