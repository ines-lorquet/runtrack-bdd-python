import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "azerty",
    database = "LaPlateforme",
)

cursor = bd.cursor()
cursor.execute("SELECT SUM(superficie) FROM etage")
result = cursor.fetchone()[0]
print("La superficie de La Plateforme est de",result,"m2")

cursor.close()