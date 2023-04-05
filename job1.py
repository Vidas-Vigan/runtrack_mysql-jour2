import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="voltigeur21",
    database="laPlateforme"
)

tableau = connection.cursor()

tableau.execute("SELECT * FROM etudiants ")
resultat = tableau.fetchall()

print(resultat)

tableau.close()
connection.close() 
