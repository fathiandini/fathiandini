import mysql.connector


def getMySqlConnection():
    return mysql.connector.connect(user='root', host='localhost', port=8889, password='root', database='restoran_csc')
#port 8080
#oassword: ''
#database: [sesuain sama database yang dibikin]