-- Tabla para USUARIOS
CREATE TABLE USUARIO (
    id_usuario INT PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Tabla para CLIENTES (Hereda de USUARIO)
CREATE TABLE CLIENTE (
    id_cliente INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nombre_cliente VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);

-- Tabla para DESTINOS
CREATE TABLE DESTINO (
    id_destino INT PRIMARY KEY,
    nombre_destino VARCHAR(100) NOT NULL,
    descripcion TEXT,
    actividades TEXT,
    costo DECIMAL(10, 2) NOT NULL
);

-- Tabla para PAQUETES TURÍSTICOS
CREATE TABLE PAQUETE_TURISTICO (
    id_paquete INT PRIMARY KEY,
    nombre_paquete VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    precio_total DECIMAL(10, 2) DEFAULT 0
);

-- Tabla de relación entre PAQUETES TURÍSTICOS y DESTINOS
CREATE TABLE PAQUETE_DESTINO (
    id_paquete INT NOT NULL,
    id_destino INT NOT NULL,
    PRIMARY KEY (id_paquete, id_destino),
    FOREIGN KEY (id_paquete) REFERENCES PAQUETE_TURISTICO(id_paquete),
    FOREIGN KEY (id_destino) REFERENCES DESTINO(id_destino)
);

-- Tabla para RESERVAS
CREATE TABLE RESERVA (
    id_reserva INT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_paquete INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    estado_reserva VARCHAR(20) DEFAULT 'Pendiente',
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),
    FOREIGN KEY (id_paquete) REFERENCES PAQUETE_TURISTICO(id_paquete)
);
