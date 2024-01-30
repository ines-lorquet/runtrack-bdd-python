import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "azerty",
    database = "LaPlateforme",
)

cursor = bd.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
result = cursor.fetchone()
print("La capacité de toutes les salles est de :",result[0])

cursor.close()