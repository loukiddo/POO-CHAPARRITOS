import hashlib
from bd import hacer_consulta

class Usuario:
    def __init__(self, id_usuario: int, nombre_usuario: str, email: str, password: str):
        self.id_usuario     = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email          = email
        self.__password     = password

    # Getters y setters
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = hashlib.sha256(password.encode('UTF-8')).hexdigest()

    # Métodos
    def registrar_usuario(self):
        """Registrar un nuevo usuario en la base de datos"""
        query = "INSERT INTO USUARIO (id_usuario, nombre_usuario, email, password) VALUES(:id_usuario, :nombre_usuario, :email, :password)"
        variables = [self.id_usuario, self.nombre_usuario, self.email, self.password]
        hacer_consulta(query, 'insert', variables)

    def iniciar_sesion(self, email: str, password: str):
        """Valida las credenciales del usuario para iniciar sesión"""
        if self.email == email and self.password == hashlib.sha256(password.encode('UTF-8')).hexdigest():
            return f"Bienvenido {self.nombre_usuario}!"
        else:
            return "Credenciales incorrectas."
        
    def actualizar_usuario(self, nombre_usuario=None, email=None, password=None):
        """Actualizar los datos del usuario en la base de datos"""
        if password:
            self.password = password  # Actualiza el password utilizando el setter
        query = "UPDATE USUARIO SET nombre_usuario = :nombre_usuario, email = :email, password = :password WHERE id_usuario = :id_usuario"
        variables = [nombre_usuario or self.nombre_usuario, email or self.email, self.password, self.id_usuario]
        hacer_consulta(query, 'update', variables)

    def eliminar_usuario(self):
        """Eliminar un usuario de la base de datos"""
        query = "DELETE FROM USUARIO WHERE id_usuario = :id_usuario"
        variables = [self.id_usuario]
        hacer_consulta(query, 'delete', variables)


class Cliente(Usuario):
    def __init__(self, id_cliente: int, nombre_cliente: str, id_usuario: int, nombre_usuario: str, email: str, password: str):
        super().__init__(id_usuario, nombre_usuario, email, password)
        self.id_cliente   = id_cliente
        self.nombre_cliente = nombre_cliente

    # Métodos
    def registrar_cliente(self):
        """Registrar un nuevo cliente en la base de datos"""
        query = "INSERT INTO CLIENTE (id_cliente, nombre_cliente, id_usuario, nombre_usuario, email) VALUES(:id_cliente, :nombre_cliente, :id_usuario, :nombre_usuario, :email)"
        variables = [self.id_cliente, self.nombre_cliente, self.id_usuario, self.nombre_usuario, self.email]
        hacer_consulta(query, 'insert', variables)

    def ver_detalles_personales(self):
        """Ver los detalles personales del cliente"""
        query = "SELECT * FROM CLIENTE WHERE id_cliente = :id_cliente"
        variables = [self.id_cliente]
        result = hacer_consulta(query, 'select', variables)
        if result:
            return result[0]  # Devuelve los detalles del cliente
        else:
            return "Cliente no encontrado."

    def iniciar_sesion(self, email: str, password: str):
        """Valida las credenciales del cliente para iniciar sesión"""
        if self.email == email and self.password == hashlib.sha256(password.encode('UTF-8')).hexdigest():
            return f"Bienvenido {self.nombre_cliente}!"
        else:
            return "Credenciales incorrectas."


class Destino:
    def __init__(self, id_destino: int, nombre_destino: str, descripcion: str, actividades: str, costo: float):
        self.id_destino     = id_destino
        self.nombre_destino = nombre_destino
        self.descripcion    = descripcion
        self.actividades    = actividades
        self.costo          = costo

    # Métodos
    def registrar_destino(self):
        """Registrar un destino en la base de datos"""
        query = "INSERT INTO DESTINO (id_destino, nombre_destino, descripcion, actividades, costo) VALUES(:id_destino, :nombre_destino, :descripcion, :actividades, :costo)"
        variables = [self.id_destino, self.nombre_destino, self.descripcion, self.actividades, self.costo]
        hacer_consulta(query, 'insert', variables)

    def ver_destinos(self):
        """Ver los destinos registrados"""
        query = "SELECT * FROM DESTINO"
        result = hacer_consulta(query, 'select')
        if result:
            return result
        else:
            return "No se encontraron destinos."


class PaqueteTuristico:
    def __init__(self, id_paquete: int, nombre_paquete: str, fecha_inicio: str, fecha_fin: str, destinos: list = []):
        self.id_paquete    = id_paquete
        self.nombre_paquete = nombre_paquete
        self.fecha_inicio   = fecha_inicio
        self.fecha_fin      = fecha_fin
        self.precio_total  = 0
        self.destinos      = destinos  # Lista de destinos asociados al paquete

    def calcular_precio_total(self):
        """Calcular el precio total del paquete sumando los costos de los destinos asociados"""
        total = sum([destino.costo for destino in self.destinos])
        self.precio_total = total
        return self.precio_total

    def registrar_paquete(self):
        """Registrar un nuevo paquete turístico en la base de datos"""
        query = "INSERT INTO PAQUETE_TURISTICO (id_paquete, nombre_paquete, fecha_inicio, fecha_fin, precio_total) VALUES(:id_paquete, :nombre_paquete, :fecha_inicio, :fecha_fin, :precio_total)"
        variables = [self.id_paquete, self.nombre_paquete, self.fecha_inicio, self.fecha_fin, self.precio_total]
        hacer_consulta(query, 'insert', variables)
        
        # Asociar destinos con el paquete
        for destino in self.destinos:
            self.asociar_destino(destino)

    def asociar_destino(self, destino):
        """Asociar un destino al paquete turístico"""
        query = "INSERT INTO PAQUETE_DESTINO (id_paquete, id_destino) VALUES(:id_paquete, :id_destino)"
        variables = [self.id_paquete, destino.id_destino]
        hacer_consulta(query, 'insert', variables)

    def ver_paquete(self):
        """Ver la información del paquete turístico junto con los destinos asociados"""
        query = "SELECT * FROM PAQUETE_TURISTICO WHERE id_paquete = :id_paquete"
        variables = [self.id_paquete]
        result = hacer_consulta(query, 'select', variables)
        
        if result:
            return result[0]  # Devuelve la información del paquete
        else:
            return "Paquete no encontrado."

    def ver_destinos_asociados(self):
        """Ver los destinos asociados a un paquete turístico"""
        query = "SELECT d.* FROM DESTINO d JOIN PAQUETE_DESTINO pd ON d.id_destino = pd.id_destino WHERE pd.id_paquete = :id_paquete"
        variables = [self.id_paquete]
        result = hacer_consulta(query, 'select', variables)
        
        if result:
            return result  # Devuelve los destinos asociados al paquete
        else:
            return "No se encontraron destinos para este paquete."
