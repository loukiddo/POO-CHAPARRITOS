-- Tabla para USUARIOS
CREATE TABLE USUARIO (
    id_usuario INT PRIMARY KEY,            -- ID único del usuario
    nombre_usuario VARCHAR(100) NOT NULL,  -- Nombre de usuario
    email VARCHAR(100) UNIQUE NOT NULL,    -- Correo electrónico único
    password VARCHAR(255) NOT NULL         -- Contraseña cifrada
);

-- Tabla para CLIENTES (Hereda de USUARIO)
CREATE TABLE CLIENTE (
    id_cliente INT PRIMARY KEY,            -- ID único del cliente
    id_usuario INT NOT NULL,               -- ID del usuario relacionado
    nombre_cliente VARCHAR(100) NOT NULL,  -- Nombre del cliente
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)  -- Relación con USUARIO
);

-- Tabla para PAQUETES TURÍSTICOS
CREATE TABLE PAQUETE_TURISTICO (
    id_paquete INT PRIMARY KEY,            -- ID único del paquete turístico
    nombre_paquete VARCHAR(100) NOT NULL,  -- Nombre del paquete
    fecha_inicio DATE NOT NULL,            -- Fecha de inicio del paquete
    fecha_fin DATE NOT NULL,               -- Fecha de fin del paquete
    precio_total DECIMAL(10, 2) DEFAULT 0  -- Precio total del paquete, con valor por defecto
);

-- Tabla para DESTINOS
CREATE TABLE DESTINO (
    id_destino INT PRIMARY KEY,            -- ID único del destino
    nombre_destino VARCHAR(100) NOT NULL,  -- Nombre del destino
    descripcion TEXT,                      -- Descripción del destino
    actividades TEXT,                      -- Actividades disponibles en el destino
    costo DECIMAL(10, 2) NOT NULL          -- Costo del destino
);

-- Tabla de relación entre PAQUETES TURÍSTICOS y DESTINOS
CREATE TABLE PAQUETE_DESTINO (
    id_paquete INT NOT NULL,               -- ID del paquete turístico
    id_destino INT NOT NULL,               -- ID del destino
    PRIMARY KEY (id_paquete, id_destino),  -- Clave primaria compuesta
    FOREIGN KEY (id_paquete) REFERENCES PAQUETE_TURISTICO(id_paquete),  -- Relación con PAQUETE_TURISTICO
    FOREIGN KEY (id_destino) REFERENCES DESTINO(id_destino)             -- Relación con DESTINO
);

-- Tabla para RESERVAS
CREATE TABLE RESERVA (
    id_reserva INT PRIMARY KEY,            -- ID único de la reserva
    id_cliente INT NOT NULL,               -- ID del cliente que hizo la reserva
    id_paquete INT NOT NULL,               -- ID del paquete reservado
    fecha_reserva DATE NOT NULL,           -- Fecha en la que se hizo la reserva
    estado_reserva VARCHAR(20) DEFAULT 'Pendiente',  -- Estado de la reserva (Pendiente, Confirmada, Cancelada)
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),  -- Relación con CLIENTE
    FOREIGN KEY (id_paquete) REFERENCES PAQUETE_TURISTICO(id_paquete)  -- Relación con PAQUETE_TURISTICO
);
