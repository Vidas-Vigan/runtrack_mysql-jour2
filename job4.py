import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="voltigeur21",
    database="maison"
)

tableau = connection.cursor()

tableau.execute("SELECT * FROM salle ")
resultat = tableau.fetchall()

print(resultat)

tableau.close()
connection.close() 
