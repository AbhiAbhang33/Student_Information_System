import mysql.connector

con=mysql.connector.connect(user="root",
                            passwd="******@24",
                            port=3306,
                            host="localhost",
                            database="*****")

con.autocommit = True
