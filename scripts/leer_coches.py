import json
import mysql.connector
from prettytable import PrettyTable

# Cargar configuración desde el archivo JSON
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
    filas = cursor.fetchall()

    # Configuración de la tabla PrettyTable
    tabla = PrettyTable()
    tabla.field_names = [i[0] for i in cursor.description]

    for fila in filas:
        tabla.add_row(fila)

    print(tabla)

    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
