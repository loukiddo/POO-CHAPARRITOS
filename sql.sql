-- Tabla de usuarios
CREATE TABLE USUARIO (
    id_usuario INT PRIMARY KEY,
    nombre_usuario VARCHAR2(100),
    email VARCHAR2(100) UNIQUE,
    password VARCHAR2(256)
);

-- Tabla de clientes (relacionada con usuarios)
CREATE TABLE CLIENTE (
    id_cliente INT PRIMARY KEY,
    nombre_cliente VARCHAR2(100),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO (id_usuario) ON DELETE CASCADE
);

-- Tabla de destinos
CREATE TABLE DESTINO (
    id_destino INT PRIMARY KEY,
    nombre_destino VARCHAR2(100),
    descripcion VARCHAR2(255),
    actividades VARCHAR2(255),
    costo FLOAT,
    paquete INT,
    FOREIGN KEY (paquete) REFERENCES PAQUETE_TURISTICO (id_paquete) ON DELETE SET NULL
);

-- Tabla de paquetes turísticos
CREATE TABLE PAQUETE_TURISTICO (
    id_paquete INT PRIMARY KEY,
    nombre_paquete VARCHAR2(100),
    fecha_inicio DATE,
    fecha_fin DATE,
    destinos VARCHAR2(255),
    precio_total FLOAT
);

-- Tabla de reservas
CREATE TABLE RESERVA (
    id_reserva INT PRIMARY KEY,
    id_cliente INT,
    id_paquete INT,
    fecha_reserva DATE,
    estado_reserva VARCHAR2(50) DEFAULT 'Pendiente',
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE (id_cliente) ON DELETE CASCADE,
    FOREIGN KEY (id_paquete) REFERENCES PAQUETE_TURISTICO (id_paquete) ON DELETE CASCADE
);
