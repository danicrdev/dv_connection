import mysql.connector as mysql
import csv


HOST = 'your host'
PORT= 'your port'
DATABASE = 'database name'
USER = 'user name'
PASSWORD = 'password'
conexion_db = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
cursor = conexion_db.cursor()

csv= csv.reader(open('your file path'))
header = next(csv)

for row in csv:
	print(row)
	cursor.execute("INSERT INTO train(id, survived, pclass, name, sex, age, sib_sp, parch, ticket, fare, cabin, embarked) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", row)

conexion_db.commit()
cursor.close()
print('exito')


