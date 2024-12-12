from bd import hacer_consulta
import hashlib

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, email, password):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def registrar_usuario(self):
        query = "INSERT INTO USUARIO (id_usuario, nombre_usuario, email, password) VALUES (:1, :2, :3, :4)"
        variables = [self.id_usuario, self.nombre_usuario, self.email, self.password]
        hacer_consulta(query, "insert", variables)

    def iniciar_sesion(self, email, password):
        query = "SELECT id_usuario, nombre_usuario, email, password FROM USUARIO WHERE email = :1 AND password = :2"
        variables = [email, self._hash_password(password)]
        result = hacer_consulta(query, "select", variables)
        return result[0] if result else None

class Cliente:
    def __init__(self, id_cliente, id_usuario, nombre_cliente):
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.nombre_cliente = nombre_cliente

    def registrar_cliente(self):
        query = "INSERT INTO CLIENTE (id_cliente, id_usuario, nombre_cliente) VALUES (:1, :2, :3)"
        variables = [self.id_cliente, self.id_usuario, self.nombre_cliente]
        hacer_consulta(query, "insert", variables)

    def ver_detalles(self):
        query = "SELECT nombre_cliente, email FROM CLIENTE WHERE id_cliente = :1"
        variables = [self.id_cliente]
        return hacer_consulta(query, "select", variables)

class Destino:
    def __init__(self, id_destino, nombre_destino, descripcion, actividades, costo, paquete=None):
        self.id_destino = id_destino
        self.nombre_destino = nombre_destino
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo
        self.paquete = paquete

    def agregar_destino(self):
        query_insert = "INSERT INTO DESTINO (id_destino, nombre_destino, descripcion, actividades, costo, id_paquete) VALUES (:1, :2, :3, :4, :5, :6)"
        query_update_precio = "UPDATE PAQUETE_TURISTICO SET PRECIO_TOTAL = PRECIO_TOTAL + :1 WHERE ID_PAQUETE = :2"
        variables_insert = [self.id_destino, self.nombre_destino, self.descripcion, self.actividades, self.costo, self.paquete if self.paquete else None]
        hacer_consulta(query_insert, 'insert', variables_insert)
        
        if self.paquete:
            hacer_consulta(query_update_precio, 'update', [self.costo, self.paquete])

    def modificar_destino(self, nombre_destino=None, descripcion=None, actividades=None, costo=None):
        query = "UPDATE DESTINO SET nombre_destino = :1, descripcion = :2, actividades = :3, costo = :4 WHERE id_destino = :5"
        variables = [nombre_destino or self.nombre_destino, descripcion or self.descripcion, actividades or self.actividades, costo or self.costo, self.id_destino]
        hacer_consulta(query, 'update', variables)

    def eliminar_destino(self):
        query_delete = "DELETE FROM DESTINO WHERE id_destino = :1"
        query_update_precio = "UPDATE PAQUETE_TURISTICO SET PRECIO_TOTAL = PRECIO_TOTAL - :1 WHERE ID_PAQUETE = :2"
        variables = [self.id_destino]
        
        if self.paquete:
            hacer_consulta(query_update_precio, 'update', [self.costo, self.paquete])

        hacer_consulta(query_delete, 'delete', variables)

class PaqueteTuristico:
    def __init__(self, id_paquete, nombre_paquete, fecha_inicio, fecha_fin):
        self.id_paquete = id_paquete
        self.nombre_paquete = nombre_paquete
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = 0

    def crear_paquete(self):
        query = "INSERT INTO PAQUETE_TURISTICO (id_paquete, nombre_paquete, fecha_inicio, fecha_fin, precio_total) VALUES (:1, :2, :3, :4, :5)"
        variables = [self.id_paquete, self.nombre_paquete, self.fecha_inicio, self.fecha_fin, self.precio_total]
        hacer_consulta(query, "insert", variables)

    def calcular_precio_total(self):
        query = "SELECT SUM(costo) FROM DESTINO WHERE id_paquete = :1"
        variables = [self.id_paquete]
        result = hacer_consulta(query, "select", variables)
        self.precio_total = result[0][0] if result and result[0][0] is not None else 0
        return self.precio_total

    def actualizar_paquete(self, nombre_paquete=None, fecha_inicio=None, fecha_fin=None):
        query = "UPDATE PAQUETE_TURISTICO SET nombre_paquete = :1, fecha_inicio = :2, fecha_fin = :3 WHERE id_paquete = :4"
        variables = [nombre_paquete or self.nombre_paquete, fecha_inicio or self.fecha_inicio, fecha_fin or self.fecha_fin, self.id_paquete]
        hacer_consulta(query, "update", variables)

    def eliminar_paquete(self):
        query = "DELETE FROM PAQUETE_TURISTICO WHERE id_paquete = :1"
        variables = [self.id_paquete]
        hacer_consulta(query, "delete", variables)

class Reserva:
    def __init__(self, id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva="Pendiente"):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = estado_reserva

    def crear_reserva(self):
        query = "INSERT INTO RESERVA (id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva) VALUES (:1, :2, :3, :4, :5)"
        variables = [self.id_reserva, self.id_cliente, self.id_paquete, self.fecha_reserva, self.estado_reserva]
        hacer_consulta(query, "insert", variables)

    def cancelar_reserva(self):
        query = "UPDATE RESERVA SET estado_reserva = 'Cancelada' WHERE id_reserva = :1"
        variables = [self.id_reserva]
        hacer_consulta(query, "update", variables)
