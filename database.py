import mysql.connector as mysql
import random

connection = mysql.connect(user="dummybot",host="localhost",database="POLE")
cursor = connection.cursor()

def getFact():
    cursor.execute("SELECT * FROM datos")
    result = cursor.fetchall()
    fact = str(result[random.randint(0,len(result))])[2:-3]
    return fact

def addFact(arg):
    cursor.execute("INSERT INTO datos(dato) VALUES('{0}')".format(arg))
    return 