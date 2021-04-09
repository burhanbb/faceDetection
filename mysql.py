import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.4',
                              database='Attendance')
cnx.close()