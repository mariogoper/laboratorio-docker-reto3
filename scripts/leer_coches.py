import json
import mysql.connector

# Cargar credenciales desde el archivo JSON
with open("config/config.json", "r") as archivo:
    db_config = json.load(archivo)

try:
    conexion = mysql.connector.connect(
        host=db_config["host"],
        port=db_config["port"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"]
    )

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM coches")

    for coche in cursor.fetchall():
        print(coche)

    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
