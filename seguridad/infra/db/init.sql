-- NebulaCorp — esquema y datos de prueba para la BBDD interna
USE nebula;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO products (name, description, price) VALUES
('Sensor T-100',  'Sensor de temperatura industrial calibrado.', 89.90),
('Sensor H-200',  'Sensor de humedad de exterior, certificado IP67.', 124.50),
('Gateway G-50',  'Gateway IoT con LoRa y MQTT.', 459.00),
('Cable shielded','Cable apantallado CAT6a 5m.', 19.95),
('Panel solar 30W','Panel fotovoltaico monocristalino 30W.', 78.00);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    password_md5 CHAR(32) NOT NULL,
    role VARCHAR(32) NOT NULL,
    note VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Hashes MD5 sin sal (didáctico — vulnerables a wordlist).
INSERT INTO users (username, password_md5, role, note) VALUES
('admin',   '59f33ab971ff3b601270a54cf609ac98', 'admin',   'Acceso al panel de administración interno.'),
('jdev',    '3fc0a7acf087f549ac2b266baf94b8b1', 'dev',     'Usuario de desarrollo. Reutiliza la misma password en SSH del bastión.'),
('ana',     'c5bb693b8a7cd71e96856b143796c66b', 'analyst', 'Analista de datos.'),
('support', '4cb9c8a8048fd02294477fcb1a41191a', 'support', 'Cuenta de soporte con password por defecto pendiente de rotar.');

CREATE TABLE secrets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skey VARCHAR(64) NOT NULL,
    svalue TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO secrets (skey, svalue) VALUES
('flag4', 'HELICE{sql_un10n_byp4ss_th3_4p1_l4y3r}'),
('vault_hint', 'El servicio vault-nebula expone /admin/dump solo desde la red de gestion.'),
('legacy_smtp', 'smtp-relay.nebulacorp.local:587 (deprecated, no usar)');

-- Permisos: el usuario appuser sólo tiene SELECT en products. Para users y
-- secrets necesita lectura adicional vía la propia consulta vulnerable (UNION).
GRANT SELECT ON nebula.* TO 'appuser'@'%';
FLUSH PRIVILEGES;
