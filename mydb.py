import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd = 'st@vemark-04'


)
cursorObject = dataBase.cursor()
#create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")
