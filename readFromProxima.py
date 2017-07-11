import mysql.connector
import datetime

cnx = mysql.connector.connect(user="dune", password="rhoades303", host="127.0.0.1", database="dune")

cursor = cnx.cursor()

query = ("SELECT operator_id, operator_name, operator_email, operator_status, created FROM operator")

cursor.execute(query)

for (operator_id, operator_name, operator_email, operator_status, created) in cursor:
    print("{} {} {} {}".format(operator_id, operator_name, operator_email, operator_status, created))
    
cursor.close()
cnx.close()