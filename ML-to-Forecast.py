import pymysql
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder

# ------------------- DataBase Connection -----------
conx = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="cars_information"
)

cur = conx.cursor()

com = """
    SELECT Car_name, Model, Operation, City, Price
    FROM cars_info
"""
# ------------------ Using Machine Learning ------------

x = []
y = []

'''Use Try and Except structure'''
try:
    '''Find all data'''
    a = cur.execute(com)
    res = cur.fetchall()

    '''Append each cars data into x and y array'''
    for car in res:
        x.append(car[:4])
        y.append(car[4])

    '''Because of Not Convert string to float we use OneHotEncoder'''
    encoder = OneHotEncoder(handle_unknown='ignore')
    x_encode = encoder.fit_transform(x).toarray()

    '''Use Decision Tree for machine learning'''
    clf = tree.DecisionTreeClassifier()
    '''Learning Machine'''
    clf.fit(x_encode, y)

    '''Take input for predict the price from car name, model, operation and city'''
    pre_price = input("Enter your car features (Car_name/Model/Operation/City): ").split("/")

    '''Because we encode the string we have to transform'''
    pre_encode = encoder.transform([pre_price]).toarray()
    '''Save predict price into answer variable'''
    answer = clf.predict(pre_encode)
    print("Predict Price:$", answer[0])


except Exception as e:
    print(e)

# -------------- Close The DataBase ---------------------
conx.close()
