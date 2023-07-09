import mysql.connector


def getMySqlConnection():
    return mysql.connector.connect(user='root', host='localhost', port=3306, password='', database='album')
#port 8080
#oassword: ''
#database: [sesuain sama database yang dibikin]