-- Tabla de Usuarios
CREATE TABLE USUARIO (
    id_usuario NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nombre_usuario VARCHAR2(100) NOT NULL,
    email VARCHAR2(100) UNIQUE NOT NULL,
    password VARCHAR2(256) NOT NULL
);

-- Tabla de Clientes
CREATE TABLE CLIENTE (
    id_cliente NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    id_usuario NUMBER NOT NULL REFERENCES USUARIO(id_usuario),
    nombre_cliente VARCHAR2(100) NOT NULL
);

-- Tabla de Destinos
CREATE TABLE DESTINO (
    id_destino NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nombre_destino VARCHAR2(100) NOT NULL,
    descripcion VARCHAR2(255),
    actividades VARCHAR2(255),
    costo NUMBER(10, 2) NOT NULL
);

-- Tabla de Paquetes Turísticos
CREATE TABLE PAQUETE_TURISTICO (
    id_paquete NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nombre_paquete VARCHAR2(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    precio_total NUMBER(10, 2) DEFAULT 0
);

-- Relación entre Paquetes y Destinos
CREATE TABLE PAQUETE_DESTINO (
    id_paquete NUMBER NOT NULL REFERENCES PAQUETE_TURISTICO(id_paquete),
    id_destino NUMBER NOT NULL REFERENCES DESTINO(id_destino),
    PRIMARY KEY (id_paquete, id_destino)
);

-- Tabla de Reservas
CREATE TABLE RESERVA (
    id_reserva NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    id_cliente NUMBER NOT NULL REFERENCES CLIENTE(id_cliente),
    id_paquete NUMBER NOT NULL REFERENCES PAQUETE_TURISTICO(id_paquete),
    fecha_reserva DATE NOT NULL,
    estado_reserva VARCHAR2(50) DEFAULT 'Pendiente'
);