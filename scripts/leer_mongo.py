from pymongo import MongoClient
from prettytable import PrettyTable

try:
    # Conexión al contenedor MongoDB usando las credenciales del Reto 8
    uri = "mongodb://mongoadmin:mongopassword@127.0.0.1:27017/?authSource=admin"
    cliente = MongoClient(uri)

    # Seleccionar la base de datos y la colección
    db = cliente["concesionario"]
    coleccion = db["coches"]

    # Obtener todos los documentos
    documentos = list(coleccion.find())

    if documentos:
        # Configurar la tabla
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Marca", "Modelo", "Color", "KM", "Precio"]

        for doc in documentos:
            tabla.add_row([
                str(doc.get("_id")),
                doc.get("marca"),
                doc.get("modelo"),
                doc.get("color"),
                doc.get("km"),
                f"{doc.get('precio')} €"
            ])

        print(tabla)
    else:
        print("No se encontraron registros en la colección 'coches'.")

    cliente.close()

except Exception as e:
    print(f"Error al conectar o leer MongoDB: {e}")
