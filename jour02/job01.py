import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "azerty",
    database = "LaPlateforme",
)

cursor = bd.cursor()
cursor.execute("SELECT * FROM etudiant")
result = cursor.fetchall()
print(result)

cursor.close()

