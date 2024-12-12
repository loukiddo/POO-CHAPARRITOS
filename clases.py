import oracledb # No olvidar instalar con "pip install oracledb"
import getpass

# CREDENCIALES
user = 'system' # Aquí cambiar por el usuario que tengan ustedes
pswd = getpass.getpass("Ingrese contraseña: ")
dsn = 'localhost/xe'

# Para hacer una consulta se requiere una query y un tipo de query. Este tipo de query puede ser 'select','insert','update','delete'
def hacer_consulta(query, tipo_query, variables=None):
    try:
        # Crear conexión
        connection = oracledb.connect(user=user, password=pswd, dsn=dsn)

        # Crear cursor
        cursor = connection.cursor()

        try:
            if tipo_query == 'select':
                cursor.execute(query)
                return cursor.fetchall()
            else:
                cursor.execute(query, variables)
                connection.commit()

        except Exception as e:
            print(f"Error al ejecutar query: {e}")
            connection.rollback()

        finally:
            # Cerrar cursor y conexión
            cursor.close()
            connection.close()

    except Exception as e:
        print(f"Hubo un error al intentar conectar a la base de datos: {e}")

# Clase Destino
class Destino:
    def __init__(self, id_destino: int, nombre_destino: str, descripcion: str, actividades: str, costo: float):
        self.id_destino = id_destino
        self.nombre_destino = nombre_destino
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo

    def agregar_destino(self):
        query = "INSERT INTO DESTINO (id_destino, nombre_destino, descripcion, actividades, costo) VALUES (:id_destino, :nombre_destino, :descripcion, :actividades, :costo)"
        variables = [self.id_destino, self.nombre_destino, self.descripcion, self.actividades, self.costo]
        hacer_consulta(query, 'insert', variables)

    def modificar_destino(self, nombre_destino=None, descripcion=None, actividades=None, costo=None):
        query = "UPDATE DESTINO SET nombre_destino = :nombre_destino, descripcion = :descripcion, actividades = :actividades, costo = :costo WHERE id_destino = :id_destino"
        variables = [nombre_destino, descripcion, actividades, costo, self.id_destino]
        hacer_consulta(query, 'update', variables)

    def eliminar_destino(self):
        query = "DELETE FROM DESTINO WHERE id_destino = :id_destino"
        variables = [self.id_destino]
        hacer_consulta(query, 'delete', variables)

# Clase PaqueteTuristico
class PaqueteTuristico:
    def __init__(self, id_paquete: int, nombre_paquete: str, fecha_inicio: str, fecha_fin: str):
        self.id_paquete = id_paquete
        self.nombre_paquete = nombre_paquete
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def crear_paquete(self):
        query = "INSERT INTO PAQUETE_TURISTICO (id_paquete, nombre_paquete, fecha_inicio, fecha_fin) VALUES (:id_paquete, :nombre_paquete, :fecha_inicio, :fecha_fin)"
        variables = [self.id_paquete, self.nombre_paquete, self.fecha_inicio, self.fecha_fin]
        hacer_consulta(query, 'insert', variables)

    def modificar_paquete(self, nombre_paquete=None, fecha_inicio=None, fecha_fin=None):
        query = "UPDATE PAQUETE_TURISTICO SET nombre_paquete = :nombre_paquete, fecha_inicio = :fecha_inicio, fecha_fin = :fecha_fin WHERE id_paquete = :id_paquete"
        variables = [nombre_paquete, fecha_inicio, fecha_fin, self.id_paquete]
        hacer_consulta(query, 'update', variables)

    def eliminar_paquete(self):
        query = "DELETE FROM PAQUETE_TURISTICO WHERE id_paquete = :id_paquete"
        variables = [self.id_paquete]
        hacer_consulta(query, 'delete', variables)

# Clase Usuario
class Usuario:
    def __init__(self, id_usuario: int, nombre_usuario: str, email: str, password: str):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.password = password

    def registrar_usuario(self):
        query = "INSERT INTO USUARIO (id_usuario, nombre_usuario, email, password) VALUES (:id_usuario, :nombre_usuario, :email, :password)"
        variables = [self.id_usuario, self.nombre_usuario, self.email, self.password]
        hacer_consulta(query, 'insert', variables)

    def actualizar_usuario(self, nombre_usuario=None, email=None, password=None):
        query = "UPDATE USUARIO SET nombre_usuario = :nombre_usuario, email = :email, password = :password WHERE id_usuario = :id_usuario"
        variables = [nombre_usuario, email, password, self.id_usuario]
        hacer_consulta(query, 'update', variables)

    def eliminar_usuario(self):
        query = "DELETE FROM USUARIO WHERE id_usuario = :id_usuario"
        variables = [self.id_usuario]
        hacer_consulta(query, 'delete', variables)

# Clase Cliente (hereda de Usuario)
class Cliente(Usuario):
    def __init__(self, id_cliente: int, nombre_usuario: str, email: str, password: str):
        super().__init__(id_cliente, nombre_usuario, email, password)

    def registrar_cliente(self):
        query = "INSERT INTO CLIENTE (id_cliente, nombre_usuario, email) VALUES (:id_cliente, :nombre_usuario, :email)"
        variables = [self.id_usuario, self.nombre_usuario, self.email]
        hacer_consulta(query, 'insert', variables)

# Clase Reserva
class Reserva:
    def __init__(self, id_reserva: int, id_cliente: int, id_paquete: int, fecha_reserva: str, estado_reserva: str):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = estado_reserva

    def crear_reserva(self):
        query = "INSERT INTO RESERVA (id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva) VALUES (:id_reserva, :id_cliente, :id_paquete, :fecha_reserva, :estado_reserva)"
        variables = [self.id_reserva, self.id_cliente, self.id_paquete, self.fecha_reserva, self.estado_reserva]
        hacer_consulta(query, 'insert', variables)

    def cancelar_reserva(self):
        query = "DELETE FROM RESERVA WHERE id_reserva = :id_reserva"
        variables = [self.id_reserva]
        hacer_consulta(query, 'delete', variables)

    def actualizar_reserva(self, fecha_reserva=None, estado_reserva=None):
        query = "UPDATE RESERVA SET fecha_reserva = :fecha_reserva, estado_reserva = :estado_reserva WHERE id_reserva = :id_reserva"
        variables = [fecha_reserva, estado_reserva, self.id_reserva]
        hacer_consulta(query, 'update', variables)
