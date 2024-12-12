from bd import hacer_consulta
import hashlib

# Clase Usuario
class Usuario:
    def __init__(self, id_usuario, nombre_usuario, email, password):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def registrar_usuario(self):
        query = "INSERT INTO USUARIO (id_usuario, nombre_usuario, email, password) VALUES (1, 'Juan Pérez', 'juan.perez@example.com', 'hashed_password')"
        variables = [self.id_usuario, self.nombre_usuario, self.email, self.password]
        hacer_consulta(query, "insert", variables)

    def iniciar_sesion(self, email, password):
        query = "SELECT id_usuario, nombre_usuario, email, password FROM USUARIO WHERE email = 'juan.perez@example.com' AND password = 'hashed_password'"
        variables = [email, self._hash_password(password)]
        result = hacer_consulta(query, "select", variables)
        return result[0] if result else None

    def ver_usuarios(self):
        query = "SELECT * FROM USUARIO"
        result = hacer_consulta(query, "select")
        if result:
            print("\n".join([f"ID: {u[0]}, Nombre: {u[1]}, Email: {u[2]}" for u in result]))
        else:
            print("No se encontraron usuarios.")

    def actualizar_usuario(self, id_usuario, nombre_usuario, email, password):
        query = "UPDATE USUARIO SET nombre_usuario = 'Carlos López', email = 'carlos.lopez@example.com', password = 'new_hashed_password' WHERE id_usuario = 1"
        variables = [nombre_usuario, email, self._hash_password(password), id_usuario]
        hacer_consulta(query, "update", variables)

    def eliminar_usuario(self, id_usuario):
        query = "DELETE FROM USUARIO WHERE id_usuario = 1"
        hacer_consulta(query, "delete", [id_usuario])


# Clase Cliente (hereda de Usuario)
class Cliente(Usuario):
    def __init__(self, id_usuario, nombre_usuario, email, password, id_cliente, nombre_cliente):
        super().__init__(id_usuario, nombre_usuario, email, password)  # Llamada al constructor de Usuario
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente

    def registrar_cliente(self):
        query = "INSERT INTO CLIENTE (id_cliente, id_usuario, nombre_cliente) VALUES (1, 1, 'Juan Cliente')"
        variables = [self.id_cliente, self.id_usuario, self.nombre_cliente]
        hacer_consulta(query, "insert", variables)

    def ver_clientes(self):
        query = "SELECT * FROM CLIENTE"
        result = hacer_consulta(query, "select")
        if result:
            print("\n".join([f"ID Cliente: {c[0]}, ID Usuario: {c[1]}, Nombre Cliente: {c[2]}" for c in result]))
        else:
            print("No se encontraron clientes.")

    def actualizar_cliente(self, id_cliente, nombre_cliente):
        query = "UPDATE CLIENTE SET nombre_cliente = 'Carlos Cliente' WHERE id_cliente = 1"
        variables = [nombre_cliente, id_cliente]
        hacer_consulta(query, "update", variables)

    def eliminar_cliente(self, id_cliente):
        query = "DELETE FROM CLIENTE WHERE id_cliente = 1"
        hacer_consulta(query, "delete", [id_cliente])


# Clase PaqueteTuristico
class PaqueteTuristico:
    def __init__(self, id_paquete, nombre_paquete, fecha_inicio, fecha_fin):
        self.id_paquete = id_paquete
        self.nombre_paquete = nombre_paquete
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = 0

    def crear_paquete(self):
        query = "INSERT INTO PAQUETE_TURISTICO (id_paquete, nombre_paquete, fecha_inicio, fecha_fin, precio_total) VALUES (1, 'Paquete Aventura', '2024-01-01', '2024-01-10', 0)"
        variables = [self.id_paquete, self.nombre_paquete, self.fecha_inicio, self.fecha_fin, self.precio_total]
        hacer_consulta(query, "insert", variables)

    def calcular_precio_total(self):
        query = "SELECT SUM(costo) FROM DESTINO WHERE id_paquete = 1"
        variables = [self.id_paquete]
        result = hacer_consulta(query, "select", variables)
        self.precio_total = result[0][0] if result and result[0][0] is not None else 0
        return self.precio_total

    def ver_paquetes(self):
        query = "SELECT * FROM PAQUETE_TURISTICO"
        result = hacer_consulta(query, "select")
        if result:
            print("\n".join([f"ID Paquete: {p[0]}, Nombre Paquete: {p[1]}, Fecha Inicio: {p[2]}, Fecha Fin: {p[3]}, Precio Total: {p[4]}" for p in result]))
        else:
            print("No se encontraron paquetes turísticos.")

    def actualizar_paquete(self, id_paquete, nombre_paquete, fecha_inicio, fecha_fin):
        query = "UPDATE PAQUETE_TURISTICO SET nombre_paquete = 'Paquete Relax', fecha_inicio = '2024-01-15', fecha_fin = '2024-01-20' WHERE id_paquete = 1"
        variables = [nombre_paquete, fecha_inicio, fecha_fin, id_paquete]
        hacer_consulta(query, "update", variables)

    def eliminar_paquete(self, id_paquete):
        query = "DELETE FROM PAQUETE_TURISTICO WHERE id_paquete = 1"
        hacer_consulta(query, "delete", [id_paquete])


# Clase Destino
class Destino:
    def __init__(self, id_destino, nombre_destino, descripcion, actividades, costo, paquete=None):
        self.id_destino = id_destino
        self.nombre_destino = nombre_destino
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo
        self.paquete = paquete

    def agregar_destino(self):
        query_insert = "INSERT INTO DESTINO (id_destino, nombre_destino, descripcion, actividades, costo) VALUES (1, 'Playa Dorada', 'Playa hermosa', 'Surf, buceo', 500)"
        variables_insert = [self.id_destino, self.nombre_destino, self.descripcion, self.actividades, self.costo]
        hacer_consulta(query_insert, 'insert', variables_insert)
        
        if self.paquete:
            query_associate = "INSERT INTO PAQUETE_DESTINO (id_paquete, id_destino) VALUES (1, 1)"
            hacer_consulta(query_associate, 'insert', [self.paquete, self.id_destino])

    def ver_destinos(self):
        query = "SELECT * FROM DESTINO"
        result = hacer_consulta(query, "select")
        if result:
            print("\n".join([f"ID Destino: {d[0]}, Nombre Destino: {d[1]}, Descripción: {d[2]}, Actividades: {d[3]}, Costo: {d[4]}" for d in result]))
        else:
            print("No se encontraron destinos.")

    def actualizar_destino(self, id_destino, nombre_destino, descripcion, actividades, costo):
        query = "UPDATE DESTINO SET nombre_destino = 'Playa Azul', descripcion = 'Playa tranquila', actividades = 'Pesca, kayak', costo = 600 WHERE id_destino = 1"
        variables = [nombre_destino, descripcion, actividades, costo, id_destino]
        hacer_consulta(query, "update", variables)

    def eliminar_destino(self, id_destino):
        query = "DELETE FROM DESTINO WHERE id_destino = 1"
        hacer_consulta(query, "delete", [id_destino])


# Clase Reserva
class Reserva:
    def __init__(self, id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva="Pendiente"):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = estado_reserva

    def crear_reserva(self):
        query = "INSERT INTO RESERVA (id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva) VALUES (1, 1, 1, '2024-12-15', 'Pendiente')"
        variables = [self.id_reserva, self.id_cliente, self.id_paquete, self.fecha_reserva, self.estado_reserva]
        hacer_consulta(query, "insert", variables)

    def cancelar_reserva(self):
        query = "UPDATE RESERVA SET estado_reserva = 'Cancelada' WHERE id_reserva = 1"
        variables = [self.id_reserva]
        hacer_consulta(query, "update", variables)

    def ver_reservas(self):
        query = "SELECT * FROM RESERVA"
        result = hacer_consulta(query, "select")
        if result:
            print("\n".join([f"ID Reserva: {r[0]}, ID Cliente: {r[1]}, ID Paquete: {r[2]}, Fecha Reserva: {r[3]}, Estado Reserva: {r[4]}" for r in result]))
        else:
            print("No se encontraron reservas.")

    def actualizar_reserva(self, id_reserva, estado_reserva):
        query = "UPDATE RESERVA SET estado_reserva = 'Confirmada' WHERE id_reserva = 1"
        variables = [estado_reserva, id_reserva]
        hacer_consulta(query, "update", variables)

    def eliminar_reserva(self, id_reserva):
        query = "DELETE FROM RESERVA WHERE id_reserva = 1"
        hacer_consulta(query, "delete", [id_reserva])
