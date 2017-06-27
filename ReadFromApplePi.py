import mysql.connector
import datetime

cnx = mysql.connector.connect(user="root", password="rhoades303", host="10.0.1.6", database="DUNE")

cursor = cnx.cursor()

query = ("SELECT * FROM 'DUNE' 'inventory'")

cursor.execute(query)

for (device_name, device_type, operator_id, created) in cursor:
    print("{}, of type {} was checked in by{}, at {}.")
    
cursor.close()
cnx.close()