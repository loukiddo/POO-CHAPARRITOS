import oracledb

# Credenciales de la base de datos
user = "system"
pswd = "Inacap2024"
dsn = "localhost/xe"

# Función para realizar consultas a la base de datos
def hacer_consulta(query, tipo_query, variables=None):
    try:
        connection = oracledb.connect(user=user, password=pswd, dsn=dsn)
        cursor = connection.cursor()

        # Ejecutar la consulta con parámetros
        if variables:
            cursor.execute(query, variables)
        else:
            cursor.execute(query)

        if tipo_query == "select":
            return cursor.fetchall()
        else:
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
