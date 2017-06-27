import mysql.connector
import datetime

cnx = mysql.connector.connect(user="root", password="Rhoades104D", host="10.0.1.6", database="DUNE")

cursor = cnx.cursor()

query = ("SELECT device_name, device_type, operator_id, created FROM inventory")

cursor.execute(query)

for (device_name, device_type, operator_id, created) in cursor:
    print("{}, of type {} was checked in by {}, at {}.".format(
        device_name, device_type, operator_id, created))
    
cursor.close()
cnx.close()