from bd import hacer_consulta
import hashlib

class Usuario:
    def __init__(self, id_usuario: int, nombre_usuario: str = None, email: str = None, password: str = None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.__password = self.hash_password(password) if password else None

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode('UTF-8')).hexdigest()

    @classmethod
    def from_db(cls, data):
        return cls(data[0], data[1], data[2], data[3])

    def registrar_usuario(self):
        query = "INSERT INTO USUARIO (id_usuario, nombre_usuario, email, password) VALUES(:id_usuario, :nombre_usuario, :email, :password)"
        variables = [self.id_usuario, self.nombre_usuario, self.email, self.__password]
        hacer_consulta(query, 'insert', variables)

    def actualizar_usuario(self, nombre_usuario=None, email=None, password=None):
        if password:
            self.__password = self.hash_password(password)
        query = "UPDATE USUARIO SET nombre_usuario = :nombre_usuario, email = :email, password = :password WHERE id_usuario = :id_usuario"
        variables = [nombre_usuario or self.nombre_usuario, email or self.email, self.__password, self.id_usuario]
        hacer_consulta(query, 'update', variables)

    def eliminar_usuario(self):
        query = "DELETE FROM USUARIO WHERE id_usuario = :id_usuario"
        hacer_consulta(query, 'delete', [self.id_usuario])

class Cliente(Usuario):
    def __init__(self, id_cliente: int, nombre_cliente: str, id_usuario: int, nombre_usuario: str = None, email: str = None, password: str = None):
        super().__init__(id_usuario, nombre_usuario, email, password)
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente

    @classmethod
    def from_db(cls, data):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5])

    def registrar_cliente(self):
        query = "INSERT INTO CLIENTE (id_cliente, nombre_cliente, id_usuario) VALUES(:id_cliente, :nombre_cliente, :id_usuario)"
        variables = [self.id_cliente, self.nombre_cliente, self.id_usuario]
        hacer_consulta(query, 'insert', variables)

    def actualizar_cliente(self, nombre_cliente=None):
        query = "UPDATE CLIENTE SET nombre_cliente = :nombre_cliente WHERE id_cliente = :id_cliente"
        variables = [nombre_cliente or self.nombre_cliente, self.id_cliente]
        hacer_consulta(query, 'update', variables)

    def eliminar_cliente(self):
        query = "DELETE FROM CLIENTE WHERE id_cliente = :id_cliente"
        hacer_consulta(query, 'delete', [self.id_cliente])

class Destino:
    def __init__(self, id_destino: int, nombre_destino: str = None, descripcion: str = None, actividades: str = None, costo: float = None, paquete: int = None):
        self.id_destino = id_destino
        self.nombre_destino = nombre_destino
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo
        self.paquete = paquete

    @classmethod
    def from_db(cls, data):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5])

    def registrar_destino(self):
        query = "INSERT INTO DESTINO (id_destino, nombre_destino, descripcion, actividades, costo, paquete) VALUES(:id_destino, :nombre_destino, :descripcion, :actividades, :costo, :paquete)"
        variables = [self.id_destino, self.nombre_destino, self.descripcion, self.actividades, self.costo, self.paquete]
        hacer_consulta(query, 'insert', variables)

    def actualizar_destino(self, nombre_destino=None, descripcion=None, actividades=None, costo=None):
        query = "UPDATE DESTINO SET nombre_destino = :nombre_destino, descripcion = :descripcion, actividades = :actividades, costo = :costo WHERE id_destino = :id_destino"
        variables = [
            nombre_destino or self.nombre_destino,
            descripcion or self.descripcion,
            actividades or self.actividades,
            costo if costo is not None else self.costo,
            self.id_destino
        ]
        hacer_consulta(query, 'update', variables)

    def eliminar_destino(self):
        query = "DELETE FROM DESTINO WHERE id_destino = :id_destino"
        hacer_consulta(query, 'delete', [self.id_destino])

class PaqueteTuristico:
    def __init__(self, id_paquete: int, nombre_paquete: str = None, fecha_inicio: str = None, fecha_fin: str = None, destinos: str = None, precio_total: float = 0):
        self.id_paquete = id_paquete
        self.nombre_paquete = nombre_paquete
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.destinos = destinos
        self.precio_total = precio_total

    @classmethod
    def from_db(cls, data):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5])

    def crear_paquete(self):
        query = "INSERT INTO PAQUETE_TURISTICO (id_paquete, nombre_paquete, fecha_inicio, fecha_fin, destinos, precio_total) VALUES(:id_paquete, :nombre_paquete, :fecha_inicio, :fecha_fin, :destinos, :precio_total)"
        variables = [self.id_paquete, self.nombre_paquete, self.fecha_inicio, self.fecha_fin, self.destinos, self.precio_total]
        hacer_consulta(query, 'insert', variables)

    def actualizar_paquete(self, nombre_paquete=None, fecha_inicio=None, fecha_fin=None, destinos=None):
        query = "UPDATE PAQUETE_TURISTICO SET nombre_paquete = :nombre_paquete, fecha_inicio = :fecha_inicio, fecha_fin = :fecha_fin, destinos = :destinos WHERE id_paquete = :id_paquete"
        variables = [
            nombre_paquete or self.nombre_paquete,
            fecha_inicio or self.fecha_inicio,
            fecha_fin or self.fecha_fin,
            destinos or self.destinos,
            self.id_paquete
        ]
        hacer_consulta(query, 'update', variables)

    def eliminar_paquete(self):
        query = "DELETE FROM PAQUETE_TURISTICO WHERE id_paquete = :id_paquete"
        hacer_consulta(query, 'delete', [self.id_paquete])

class Reserva:
    def __init__(self, id_reserva: int, id_cliente: int = None, id_paquete: int = None, fecha_reserva: str = None, estado_reserva: str = "Pendiente"):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = estado_reserva

    @classmethod
    def from_db(cls, data):
        return cls(data[0], data[1], data[2], data[3], data[4])

    def crear_reserva(self):
        query = "INSERT INTO RESERVA (id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva) VALUES(:id_reserva, :id_cliente, :id_paquete, :fecha_reserva, :estado_reserva)"
        variables = [self.id_reserva, self.id_cliente, self.id_paquete, self.fecha_reserva, self.estado_reserva]
        hacer_consulta(query, 'insert', variables)

    def actualizar_reserva(self, fecha_reserva=None, estado_reserva=None):
        query = "UPDATE RESERVA SET fecha_reserva = :fecha_reserva, estado_reserva = :estado_reserva WHERE id_reserva = :id_reserva"
        variables = [
            fecha_reserva or self.fecha_reserva,
            estado_reserva or self.estado_reserva,
            self.id_reserva
        ]
        hacer_consulta(query, 'update', variables)

    def eliminar_reserva(self):
        query = "DELETE FROM RESERVA WHERE id_reserva = :id_reserva"
        hacer_consulta(query, 'delete', [self.id_reserva])
