from clases import Usuario, Cliente, Destino, PaqueteTuristico, Reserva
from bd import hacer_consulta

def create_usuario():
    id_usuario = int(input("ID Usuario: "))
    nombre_usuario = input("Nombre del Usuario: ")
    email = input("Email: ")
    password = input("Contraseña: ")

    usuario = Usuario(id_usuario, nombre_usuario, email, password)
    try:
        usuario.registrar_usuario()
        print("Usuario creado correctamente.")
    except Exception as e:
        print(f"Error al crear usuario: {e}")

def read_usuario():
    id_usuario = int(input("ID Usuario a buscar: "))
    query = "SELECT * FROM USUARIO WHERE id_usuario = :id_usuario"
    try:
        result = hacer_consulta(query, 'select', [id_usuario])
        if result:
            print("Usuario encontrado:", result[0])
        else:
            print("Usuario no encontrado.")
    except Exception as e:
        print(f"Error al buscar usuario: {e}")

def update_usuario():
    id_usuario = int(input("ID Usuario a actualizar: "))
    nombre_usuario = input("Nuevo Nombre (dejar vacío para no cambiar): ")
    email = input("Nuevo Email (dejar vacío para no cambiar): ")
    password = input("Nueva Contraseña (dejar vacío para no cambiar): ")

    query = "SELECT * FROM USUARIO WHERE id_usuario = :id_usuario"
    result = hacer_consulta(query, 'select', [id_usuario])
    if not result:
        print("Usuario no encontrado.")
        return

    usuario = Usuario(*result[0])
    usuario.actualizar_usuario(
        nombre_usuario=nombre_usuario if nombre_usuario else None,
        email=email if email else None,
        password=password if password else None
    )
    print("Usuario actualizado correctamente.")

def delete_usuario():
    id_usuario = int(input("ID Usuario a eliminar: "))
    usuario = Usuario(id_usuario, "", "", "")
    try:
        usuario.eliminar_usuario()
        print("Usuario eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")

# Similar lógica para Cliente, Destino, PaqueteTuristico y Reserva

def create_cliente():
    id_cliente = int(input("ID Cliente: "))
    nombre_cliente = input("Nombre del Cliente: ")
    id_usuario = int(input("ID Usuario asociado: "))
    query = "SELECT * FROM USUARIO WHERE id_usuario = :id_usuario"
    result = hacer_consulta(query, 'select', [id_usuario])
    if not result:
        print("Usuario no encontrado. Debe registrar primero al usuario.")
        return
    usuario_data = result[0]
    cliente = Cliente(id_cliente, nombre_cliente, *usuario_data)
    try:
        cliente.registrar_cliente()
        print("Cliente creado correctamente.")
    except Exception as e:
        print(f"Error al crear cliente: {e}")

def delete_cliente():
    id_cliente = int(input("ID Cliente a eliminar: "))
    cliente = Cliente(id_cliente, "", 0, "", "", "")
    try:
        cliente.eliminar_usuario()
        print("Cliente eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")

# CRUD para Destino
def create_destino():
    id_destino = int(input("ID Destino: "))
    nombre_destino = input("Nombre del Destino: ")
    descripcion = input("Descripción: ")
    actividades = input("Actividades: ")
    costo = float(input("Costo: "))

    destino = Destino(id_destino, nombre_destino, descripcion, actividades, costo)
    try:
        destino.registrar_destino()
        print("Destino registrado correctamente.")
    except Exception as e:
        print(f"Error al registrar destino: {e}")

def delete_destino():
    id_destino = int(input("ID Destino a eliminar: "))
    destino = Destino(id_destino, "", "", "", 0)
    try:
        destino.eliminar_destino()
        print("Destino eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar destino: {e}")

# CRUD para Paquete Turístico
def create_paquete():
    id_paquete = int(input("ID Paquete: "))
    nombre_paquete = input("Nombre del Paquete: ")
    fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de Fin (YYYY-MM-DD): ")
    destinos = input("Destinos (separados por comas): ")

    paquete = PaqueteTuristico(id_paquete, nombre_paquete, fecha_inicio, fecha_fin, destinos)
    try:
        paquete.crear_paquete()
        print("Paquete creado correctamente.")
    except Exception as e:
        print(f"Error al crear paquete: {e}")

def delete_paquete():
    id_paquete = int(input("ID Paquete a eliminar: "))
    paquete = PaqueteTuristico(id_paquete, "", "", "", "")
    try:
        paquete.eliminar_paquete()
        print("Paquete eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar paquete: {e}")

# CRUD para Reserva
def create_reserva():
    id_reserva = int(input("ID Reserva: "))
    id_cliente = int(input("ID Cliente: "))
    id_paquete = int(input("ID Paquete: "))
    fecha_reserva = input("Fecha de Reserva (YYYY-MM-DD): ")
    estado_reserva = input("Estado de Reserva (Pendiente/Confirmada): ")

    reserva = Reserva(id_reserva, id_cliente, id_paquete, fecha_reserva, estado_reserva)
    try:
        reserva.crear_reserva()
        print("Reserva creada correctamente.")
    except Exception as e:
        print(f"Error al crear reserva: {e}")

def delete_reserva():
    id_reserva = int(input("ID Reserva a eliminar: "))
    reserva = Reserva(id_reserva, 0, 0, "", "")
    try:
        reserva.eliminar_reserva()
        print("Reserva eliminada correctamente.")
    except Exception as e:
        print(f"Error al eliminar reserva: {e}")

# Menú principal para ejecutar funciones CRUD
def menu():
    opciones = {
        "1": create_usuario,
        "2": read_usuario,
        "3": update_usuario,
        "4": delete_usuario,
        "5": create_cliente,
        "6": delete_cliente,
        "7": create_destino,
        "8": delete_destino,
        "9": create_paquete,
        "10": delete_paquete,
        "11": create_reserva,
        "12": delete_reserva,
    }

    while True:
        print("""
        Menú:
        1. Crear Usuario
        2. Leer Usuario
        3. Actualizar Usuario
        4. Eliminar Usuario
        5. Crear Cliente
        6. Eliminar Cliente
        7. Crear Destino
        8. Eliminar Destino
        9. Crear Paquete Turístico
        10. Eliminar Paquete Turístico
        11. Crear Reserva
        12. Eliminar Reserva
        13. Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "13":
            print("Saliendo del sistema.")
            break

        funcion = opciones.get(opcion)
        if funcion:
            funcion()
        else:
            print("Opción no válida.")

# Ejecutar el menú si se ejecuta directamente el script
if __name__ == "__main__":
    menu()