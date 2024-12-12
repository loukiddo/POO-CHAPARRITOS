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
        self.id_destino = id_destino
        self.nombre_destino = nombre_destino
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo

    def registrar_destino(self):
        """Registrar un destino en la base de datos"""
        query = "INSERT INTO DESTINO (id_destino, nombre_destino, descripcion, actividades, costo) VALUES(:id_destino, :nombre_destino, :descripcion, :actividades, :costo)"
        variables = [self.id_destino, self.nombre_destino, self.descripcion, self.actividades, self.costo]
        hacer_consulta(query, 'insert', variables)

    def ver_destinos(self):
        """Ver todos los destinos disponibles"""
        query = "SELECT * FROM DESTINO"
        result = hacer_consulta(query, 'select')
        if result:
            return result  # Devuelve la lista de destinos
        else:
            return "No se encontraron destinos."


class PaqueteTuristico:
    def __init__(self, id_paquete: int, nombre_paquete: str, fecha_inicio: str, fecha_fin: str, destinos: str):
        """
        El campo destinos se almacenará como una cadena de texto separada por comas.
        Ejemplo: 'Playa del Sol, Montaña Nevada'.
        """
        self.id_paquete = id_paquete
        self.nombre_paquete = nombre_paquete
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.destinos = destinos  # Cadena de texto con destinos separados por comas
        self.precio_total = 0

    def crear_paquete(self):
        """Registrar un paquete turístico en la base de datos"""
        query = "INSERT INTO PAQUETE_TURISTICO (id_paquete, nombre_paquete, fecha_inicio, fecha_fin, destinos, precio_total) VALUES(:id_paquete, :nombre_paquete, :fecha_inicio, :fecha_fin, :destinos, :precio_total)"
        variables = [self.id_paquete, self.nombre_paquete, self.fecha_inicio, self.fecha_fin, self.destinos, self.precio_total]
        hacer_consulta(query, 'insert', variables)

    def calcular_precio_total(self):
        """Calcular el precio total del paquete turístico basado en los destinos"""
        destinos = self.destinos.split(",")  # Convertimos la cadena en una lista de destinos
        precio_total = 0
        for destino in destinos:
            # Suponemos que los destinos ya están registrados en la base de datos
            query = "SELECT costo FROM DESTINO WHERE nombre_destino = :destino"
            variables = [destino.strip()]  # Limpiamos el espacio en blanco alrededor del nombre del destino
            result = hacer_consulta(query, 'select', variables)
            if result:
                precio_total += result[0][0]
        self.precio_total = precio_total
        return self.precio_total

    def ver_paquetes(self):
        """Ver todos los paquetes turísticos disponibles"""
        query = "SELECT * FROM PAQUETE_TURISTICO"
        result = hacer_consulta(query, 'select')
        if result:
            return result  # Devuelve la lista de paquetes turísticos
        else:
            return "No se encontraron paquetes turísticos."

    def actualizar_paquete(self, nombre_paquete=None, fecha_inicio=None, fecha_fin=None, destinos=None):
        """Actualizar un paquete turístico en la base de datos"""
        query = "UPDATE PAQUETE_TURISTICO SET nombre_paquete = :nombre_paquete, fecha_inicio = :fecha_inicio, fecha_fin = :fecha_fin, destinos = :destinos WHERE id_paquete = :id_paquete"
        variables = [nombre_paquete or self.nombre_paquete, fecha_inicio or self.fecha_inicio, fecha_fin or self.fecha_fin, destinos or self.destinos, self.id_paquete]
        hacer_consulta(query, 'update', variables)

    def eliminar_paquete(self):
        """Eliminar un paquete turístico de la base de datos"""
        query = "DELETE FROM PAQUETE_TURISTICO WHERE id_paquete = :id_paquete"
        variables = [self.id_paquete]
        hacer_consulta(query, 'delete', variables)


class Reserva:
    def __init__(self, id_reserva: int, id_cliente: int, id_paquete: int, fecha_reserva: str, estado_reserva: str = "Pendiente"):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = estado_reserva

    def crear_reserva(self):
        """Registrar una nueva reserva en la base de datos"""
        query = "INSERT INTO RESERVA (id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva) VALUES(:id_reserva, :id_cliente, :id_paquete, :fecha_reserva, :estado_reserva)"
        variables = [self.id_reserva, self.id_cliente, self.id_paquete, self.fecha_reserva, self.estado_reserva]
        hacer_consulta(query, 'insert', variables)

    def cancelar_reserva(self):
        """Cancelar una reserva"""
        query = "UPDATE RESERVA SET estado_reserva = 'Cancelada' WHERE id_reserva = :id_reserva"
        variables = [self.id_reserva]
        hacer_consulta(query, 'update', variables)

    def ver_reservas(self):
        """Ver todas las reservas realizadas"""
        query = "SELECT * FROM RESERVA"
        result = hacer_consulta(query, 'select')
        if result:
            return result  # Devuelve la lista de reservas
        else:
            return "No se encontraron reservas."
