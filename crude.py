from bd import hacer_consulta
from clases import Usuario, Cliente, Destino, PaqueteTuristico, Reserva

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

# CRUD para Cliente
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

def read_cliente():
    id_cliente = int(input("ID Cliente a buscar: "))
    query = "SELECT * FROM CLIENTE WHERE id_cliente = :id_cliente"
    try:
        result = hacer_consulta(query, 'select', [id_cliente])
        if result:
            print("Cliente encontrado:", result[0])
        else:
            print("Cliente no encontrado.")
    except Exception as e:
        print(f"Error al buscar cliente: {e}")

def update_cliente():
    id_cliente = int(input("ID Cliente a actualizar: "))
    nombre_cliente = input("Nuevo Nombre (dejar vacío para no cambiar): ")

    query = "SELECT * FROM CLIENTE WHERE id_cliente = :id_cliente"
    result = hacer_consulta(query, 'select', [id_cliente])
    if not result:
        print("Cliente no encontrado.")
        return

    cliente = Cliente(id_cliente, nombre_cliente, *result[0][2:])
    cliente.nombre_cliente = nombre_cliente if nombre_cliente else cliente.nombre_cliente
    cliente.registrar_cliente()
    print("Cliente actualizado correctamente.")

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

def read_destino():
    id_destino = int(input("ID Destino a buscar: "))
    query = "SELECT * FROM DESTINO WHERE id_destino = :id_destino"
    try:
        result = hacer_consulta(query, 'select', [id_destino])
        if result:
            print("Destino encontrado:", result[0])
        else:
            print("Destino no encontrado.")
    except Exception as e:
        print(f"Error al buscar destino: {e}")

def update_destino():
    id_destino = int(input("ID Destino a actualizar: "))
    nombre_destino = input("Nuevo Nombre (dejar vacío para no cambiar): ")
    descripcion = input("Nueva Descripción (dejar vacío para no cambiar): ")
    actividades = input("Nuevas Actividades (dejar vacío para no cambiar): ")
    costo = input("Nuevo Costo (dejar vacío para no cambiar): ")

    query = "SELECT * FROM DESTINO WHERE id_destino = :id_destino"
    result = hacer_consulta(query, 'select', [id_destino])
    if not result:
        print("Destino no encontrado.")
        return

    destino = Destino(*result[0])
    destino.actualizar_destino(
        nombre_destino=nombre_destino if nombre_destino else None,
        descripcion=descripcion if descripcion else None,
        actividades=actividades if actividades else None,
        costo=float(costo) if costo else None
    )
    print("Destino actualizado correctamente.")

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

def read_paquete():
    id_paquete = int(input("ID Paquete a buscar: "))
    query = "SELECT * FROM PAQUETE_TURISTICO WHERE id_paquete = :id_paquete"
    try:
        result = hacer_consulta(query, 'select', [id_paquete])
        if result:
            print("Paquete encontrado:", result[0])
        else:
            print("Paquete no encontrado.")
    except Exception as e:
        print(f"Error al buscar paquete: {e}")

def update_paquete():
    id_paquete = int(input("ID Paquete a actualizar: "))
    nombre_paquete = input("Nuevo Nombre (dejar vacío para no cambiar): ")
    fecha_inicio = input("Nueva Fecha de Inicio (dejar vacío para no cambiar): ")
    fecha_fin = input("Nueva Fecha de Fin (dejar vacío para no cambiar): ")
    destinos = input("Nuevos Destinos (dejar vacío para no cambiar): ")

    query = "SELECT * FROM PAQUETE_TURISTICO WHERE id_paquete = :id_paquete"
    result = hacer_consulta(query, 'select', [id_paquete])
    if not result:
        print("Paquete no encontrado.")
        return

    paquete = PaqueteTuristico(*result[0])
    paquete.actualizar_paquete(
        nombre_paquete=nombre_paquete if nombre_paquete else None,
        fecha_inicio=fecha_inicio if fecha_inicio else None,
        fecha_fin=fecha_fin if fecha_fin else None,
        destinos=destinos if destinos else None
    )
    print("Paquete actualizado correctamente.")

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

def read_reserva():
    id_reserva = int(input("ID Reserva a buscar: "))
    query = "SELECT * FROM RESERVA WHERE id_reserva = :id_reserva"
    try:
        result = hacer_consulta(query, 'select', [id_reserva])
        if result:
            print("Reserva encontrada:", result[0])
        else:
            print("Reserva no encontrada.")
    except Exception as e:
        print(f"Error al buscar reserva: {e}")

def update_reserva():
    id_reserva = int(input("ID Reserva a actualizar: "))
    id_cliente = input("Nuevo ID Cliente (dejar vacío para no cambiar): ")
    id_paquete = input("Nuevo ID Paquete (dejar vacío para no cambiar): ")
    fecha_reserva = input("Nueva Fecha de Reserva (dejar vacío para no cambiar): ")
    estado_reserva = input("Nuevo Estado (dejar vacío para no cambiar): ")

    query = "SELECT * FROM RESERVA WHERE id_reserva = :id_reserva"
    result = hacer_consulta(query, 'select', [id_reserva])
    if not result:
        print("Reserva no encontrada.")
        return

    reserva = Reserva(*result[0])
    reserva.actualizar_reserva(
        fecha_reserva=fecha_reserva if fecha_reserva else None,
        estado_reserva=estado_reserva if estado_reserva else None
    )
    print("Reserva actualizada correctamente.")

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
        "6": read_cliente,
        "7": update_cliente,
        "8": delete_cliente,
        "9": create_destino,
        "10": read_destino,
        "11": update_destino,
        "12": delete_destino,
        "13": create_paquete,
        "14": read_paquete,
        "15": update_paquete,
        "16": delete_paquete,
        "17": create_reserva,
        "18": read_reserva,
        "19": update_reserva,
        "20": delete_reserva,
    }

    while True:
        print("""
        Menú:
        1. Crear Usuario
        2. Leer Usuario
        3. Actualizar Usuario
        4. Eliminar Usuario
        5. Crear Cliente
        6. Leer Cliente
        7. Actualizar Cliente
        8. Eliminar Cliente
        9. Crear Destino
        10. Leer Destino
        11. Actualizar Destino
        12. Eliminar Destino
        13. Crear Paquete Turístico
        14. Leer Paquete Turístico
        15. Actualizar Paquete Turístico
        16. Eliminar Paquete Turístico
        17. Crear Reserva
        18. Leer Reserva
        19. Actualizar Reserva
        20. Eliminar Reserva
        21. Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "21":
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
