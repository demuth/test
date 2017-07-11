import mysql.connector
import datetime

cnx = mysql.connector.connect(user="dune", password="CENSORED", host="127.0.0.1", database="dune")

cursor = cnx.cursor()

query = ("SELECT operator_id, operator_name, operator_email, operator_status, created FROM operator")

cursor.execute(query)

for (operator_id, operator_name, operator_email, operator_status, created) in cursor:
    print("{} {} {} {} {}".format(operator_id, operator_name, operator_email, operator_status, created))

#Write to Proxima starts here
name = 'John Smith'
email = 'John.Smith@someEmail.io'
status = 'inactive'
created = '2017-07-11 16:35:27'

sql = "INSERT into operator VALUES(null, '%s', '%s', '%s', '%s')"%\
    (name, email, status, created)

number_of_rows = cursor.execute(sql)
cnx.commit()

cursor.close()
cnx.close()