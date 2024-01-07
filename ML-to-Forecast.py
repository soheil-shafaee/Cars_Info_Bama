import pymysql
from sklearn import tree


conx = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="cars_information"
)

cur = conx.cursor()

com = """
    SELECT Car_name, Model, Operation, City
    FROM cars_info
"""

try:
    a = cur.execute(com)
    x = cur.fetchall()
    y = input("Enter cars_name, model, operation, city ((Use {/} to separate)): ").split("/")
    clf = tree.DecisionTreeClassifier()
    clf.fit(x, y)

    print(clf.predict(y))

except Exception as e:
    print(e)

conx.close()
