
create database buenosasesores;
use buenosasesores;
CREATE TABLE TEMA(
   id_tema INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   nombre VARCHAR(255),
   dificultad INT
   );
CREATE TABLE ASESOR(
   id_asesor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   nombre VARCHAR(255),
   email VARCHAR(255) UNIQUE,
   contrasenia VARCHAR(255),
   nombre_usuario VARCHAR(255) UNIQUE,
   tarifa FLOAT
   );
 CREATE TABLE ASESORADO(
   id_asesorado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   nombre VARCHAR(255),
   email VARCHAR(255) UNIQUE,
   contrasenia VARCHAR(255),
   nombre_usuario VARCHAR(255) UNIQUE
   );  
CREATE TABLE TEMASDELASESOR(
   id_asesor INT,
   id_tema INT,
   FOREIGN KEY (id_asesor) REFERENCES ASESOR(id_asesor),
   FOREIGN KEY (id_tema) REFERENCES TEMA(id_tema)
   );
   
   CREATE TABLE ASESORIA(
   id_asesor INT,
   id_asesorado INT,
   fecha DATETIME,
   confirmada BOOLEAN DEFAULT (FALSE),
   FOREIGN KEY (id_asesor) REFERENCES ASESOR(id_asesor),
   FOREIGN KEY (id_asesorado) REFERENCES ASESORADO(id_asesorado)   
   ); 
   -- Registros
INSERT INTO TEMA (nombre, dificultad) VALUES ('Machine Learning Avanzado', 5),
											 ('Deep Learning con TensorFlow', 5),
                                             ('Blockchain para negocios', 4),
                                             ('Ciberseguridad ética', 4),
                                             ('Desarrollo con Rust', 3),
                                             ('Big Data con Spark', 5),
                                             ('Arquitectura de microservicios', 4),
                                             ('DevOps y CI/CD', 3),
                                             ('Inteligencia Artificial Generativa', 5),
                                             ('Programación cuántica básica', 5),
                                             ('Diseño UX/UI avanzado', 2),
                                             ('Marketing digital con IA', 2),
                                             ('Finanzas descentralizadas (DeFi)', 4),
                                             ('Realidad aumentada con Unity', 3),
                                             ('IoT y Edge Computing', 4),
                                             ('Análisis de sentimientos con NLP', 4),
                                             ('Ética en inteligencia artificial', 2),
                                             ('Scrum y gestión ágil', 1),
                                             ('Bases de datos NoSQL', 3),
                                             ('Computación en la nube (AWS/Azure)', 3);
										
INSERT INTO ASESOR (nombre, email, contrasenia, nombre_usuario, tarifa) VALUES ('Dra. Valentina Fuentes', 'valentina.fuentes@consultor.com', 'passVal2024', 'vfuentes', 85.50),
                                                                               ('Ing. Héctor Morales', 'hector.morales@asesor.com', 'hectorSecure', 'hmorales', 120.00),
                                                                               ('Mtra. Karina Jiménez', 'karina.jimenez@tech.com', 'kj2024pass', 'kjimenez', 95.75),
                                                                               ('Dr. Fernando Castro', 'fernando.castro@data.com', 'fcastro123', 'fcastro', 150.00),
                                                                               ('Lic. Daniela Rojas', 'daniela.rojas@web.com', 'drojas2024', 'drojas', 70.00),
                                                                               ('Mtro. Ricardo Núñez', 'ricardo.nunez@cloud.com', 'rnunez456', 'rnunez', 110.50),
                                                                               ('Ing. Sofía Beltrán', 'sofia.beltran@ia.com', 'sbeltransafe', 'sbeltran', 130.00),
                                                                               ('Dr. Alejandro Pineda', 'alejandro.pineda@seguridad.com', 'apineda789', 'apineda', 140.00),
                                                                               ('Mtra. Gabriela Luna', 'gabriela.luna@startup.com', 'gluna2024', 'gluna', 88.00),
                                                                               ('Ing. Mauricio Serrano', 'mauricio.serrano@block.com', 'mserranopass', 'mserrano', 105.00),
                                                                               ('Dra. Laura Espinoza', 'laura.espinoza@analytics.com', 'lespinoza2024', 'lespinoza', 125.00),
                                                                               ('Mtro. Andrés Márquez', 'andres.marquez@agile.com', 'amarquez78', 'amarquez', 65.00),
                                                                               ('Ing. Patricia Soto', 'patricia.soto@devops.com', 'psoto1234', 'psoto', 98.50),
                                                                               ('Dr. Raúl Méndez', 'raul.mendez@quantum.com', 'rmendez2024', 'rmendez', 200.00),
                                                                               ('Mtra. Cecilia Herrera', 'cecilia.herrera@uxui.com', 'cherrera55', 'cherrera', 82.00),
                                                                               ('Lic. Tomás Gálvez', 'tomas.galvez@marketing.com', 'tgalvez99', 'tgalvez', 60.00),
                                                                               ('Ing. Natalia Campos', 'natalia.campos@iot.com', 'ncamposiot', 'ncampos', 115.00),
                                                                               ('Dra. Jimena Ortiz', 'jimena.ortiz@fintech.com', 'jortiz2024', 'jortiz', 135.00),
                                                                               ('Mtro. Luis Enrique Ramos', 'luis.ramos@realidad.com', 'lramos2024', 'lramos', 90.00),
                                                                               ('Ing. Claudia Vásquez', 'claudia.vasquez@seguridad.com', 'cvasquez44', 'cvasquez', 145.00);
                                                                               
INSERT INTO ASESORADO (nombre, email, contrasenia, nombre_usuario) VALUES ('Carlos Méndez Pérez', 'carlos.mendez@estudiante.com', 'carlos2024', 'cmendez'),
																		  ('Ana Lucía Gómez', 'ana.gomez@aprendiz.com', 'anagomez123', 'agomez'),
                                                                          ('Javier Rodríguez Soto', 'javier.rodriguez@alumno.com', 'jrodriguez2024', 'jrodriguez'),
                                                                          ('Mariana Flores López', 'mariana.flores@tech.com', 'mflores2024', 'mflores'),
                                                                          ('Roberto Sánchez Cruz', 'roberto.sanchez@dev.com', 'rsanchez456', 'rsanchez'),
                                                                          ('Fernanda Castillo Mora', 'fernanda.castillo@data.com', 'fcastillo789', 'fcastillo'),
                                                                          ('Diego Herrera Vega', 'diego.herrera@startup.com', 'dherrera2024', 'dherrera'),
                                                                          ('Valentina Ruiz Paz', 'valentina.ruiz@innovacion.com', 'vruiz123', 'vruiz'),
                                                                          ('Oscar Martínez Gil', 'oscar.martinez@fisica.com', 'omartinez2024', 'omartinez'),
                                                                          ('Regina Quiroz Solís', 'regina.quiroz@matematicas.com', 'rquiroz99', 'rquiroz'),
                                                                          ('Emilio Navarro Ríos', 'emilio.navarro@ingenieria.com', 'enavarro2024', 'enavarro'),
                                                                          ('Lucía Villalobos Díaz', 'lucia.villalobos@ciencias.com', 'lvillalobos', 'lvillalobos'),
                                                                          ('Adrián Montero León', 'adrian.montero@emprende.com', 'amontero88', 'amontero'),
                                                                          ('Daniela Paredes Mora', 'daniela.paredes@code.com', 'dparedes2024', 'dparedes'),
                                                                          ('Sebastián Rangel Cruz', 'sebastian.rangel@ai.com', 'srangel123', 'srangel'),
                                                                          ('Camila Serrato López', 'camila.serrato@cloud.com', 'cserrato2024', 'cserrato'),
                                                                          ('Nicolás Fuentes Alvarado', 'nicolas.fuentes@blockchain.com', 'nfuentes2024', 'nfuentes'),
                                                                          ('Julieta Aguirre Solano', 'julieta.aguirre@design.com', 'jaguirre55', 'jaguirre'),
                                                                          ('Mateo Cárdenas Rojas', 'mateo.cardenas@iot.com', 'mcardenas2024', 'mcardenas'),
                                                                          ('Renata Sandoval León', 'renata.sandoval@fintech.com', 'rsandoval44', 'rsandoval');																			
-- 50 registros
INSERT INTO TEMASDELASESOR (id_asesor, id_tema) VALUES
(1, 1), (1, 9), (1, 16),  -- Valentina: ML, IA Generativa, NLP
(2, 5), (2, 7), (2, 8),   -- Héctor: Rust, Microservicios, DevOps
(3, 3), (3, 13), (3, 17), -- Karina: Blockchain, DeFi, Ética IA
(4, 2), (4, 10), (4, 20), -- Fernando: Deep Learning, Computación cuántica, Cloud
(5, 11), (5, 12),         -- Daniela: UX/UI, Marketing digital
(6, 4), (6, 18), (6, 19), -- Ricardo: Ciberseguridad, Scrum, NoSQL
(7, 1), (7, 9), (7, 16),  -- Sofía: ML, IA Generativa, NLP
(8, 4), (8, 14), (8, 15), -- Alejandro: Ciberseguridad, Realidad aumentada, IoT
(9, 11), (9, 12),         -- Gabriela: UX/UI, Marketing digital
(10, 3), (10, 13),        -- Mauricio: Blockchain, DeFi
(11, 6), (11, 20),        -- Laura: Big Data, Cloud
(12, 18), (12, 17),       -- Andrés: Scrum, Ética IA
(13, 7), (13, 8), (13, 19), -- Patricia: Microservicios, DevOps, NoSQL
(14, 10), (14, 2),        -- Raúl: Computación cuántica, Deep Learning
(15, 11), (15, 12),       -- Cecilia: UX/UI, Marketing digital
(16, 12), (16, 9),        -- Tomás: Marketing digital, IA Generativa
(17, 14), (17, 15), (17, 19), -- Natalia: Realidad aumentada, IoT, NoSQL
(18, 13), (18, 3),        -- Jimena: DeFi, Blockchain
(19, 14), (19, 2),        -- Luis: Realidad aumentada, Deep Learning
(20, 4), (20, 18);        -- Claudia: Ciberseguridad, Scrum

INSERT INTO ASESORIA (id_asesor, id_asesorado, fecha, confirmada) VALUES
(1, 3, '2025-01-15 10:00:00', TRUE),
(2, 5, '2025-01-20 15:30:00', FALSE),
(3, 7, '2025-01-22 09:00:00', TRUE),
(4, 2, '2025-01-25 11:15:00', TRUE),
(5, 9, '2025-01-28 16:45:00', FALSE),
(6, 1, '2025-02-01 10:30:00', TRUE),
(7, 4, '2025-02-05 14:00:00', TRUE),
(8, 6, '2025-02-08 12:30:00', FALSE),
(9, 8, '2025-02-10 09:45:00', TRUE),
(10, 10, '2025-02-12 17:00:00', TRUE),
(11, 12, '2025-02-15 11:00:00', FALSE),
(12, 14, '2025-02-18 15:00:00', TRUE),
(13, 16, '2025-02-20 13:15:00', TRUE),
(14, 18, '2025-02-22 10:00:00', FALSE),
(15, 20, '2025-02-25 16:30:00', TRUE),
(16, 1, '2025-02-28 09:30:00', TRUE),
(17, 3, '2025-03-03 14:45:00', FALSE),
(18, 5, '2025-03-05 11:00:00', TRUE),
(19, 7, '2025-03-08 15:15:00', TRUE),
(20, 9, '2025-03-10 10:30:00', TRUE),
(1, 11, '2025-03-12 13:00:00', FALSE),
(2, 13, '2025-03-15 12:15:00', TRUE),
(3, 15, '2025-03-18 17:30:00', TRUE),
(4, 17, '2025-03-20 09:00:00', FALSE),
(5, 19, '2025-03-22 14:00:00', TRUE),
(6, 2, '2025-03-25 11:45:00', TRUE),
(7, 4, '2025-03-28 16:00:00', TRUE),
(8, 6, '2025-04-01 10:15:00', FALSE),
(9, 8, '2025-04-03 13:30:00', TRUE),
(10, 10, '2025-04-06 15:45:00', TRUE),
(11, 12, '2025-04-09 09:00:00', FALSE),
(12, 14, '2025-04-11 12:00:00', TRUE),
(13, 16, '2025-04-14 17:15:00', TRUE),
(14, 18, '2025-04-16 10:30:00', FALSE),
(15, 20, '2025-04-18 14:45:00', TRUE),
(16, 1, '2025-04-21 11:00:00', TRUE),
(17, 3, '2025-04-23 16:30:00', TRUE),
(18, 5, '2025-04-25 09:15:00', FALSE),
(19, 7, '2025-04-28 13:00:00', TRUE),
(20, 9, '2025-04-30 15:30:00', TRUE),
(1, 2, '2025-05-03 10:00:00', TRUE),
(2, 4, '2025-05-06 14:15:00', FALSE),
(3, 6, '2025-05-09 12:45:00', TRUE),
(4, 8, '2025-05-12 17:30:00', TRUE),
(5, 10, '2025-05-15 09:30:00', FALSE),
(6, 12, '2025-05-18 11:15:00', TRUE),
(7, 14, '2025-05-21 15:00:00', TRUE),
(8, 16, '2025-05-24 10:45:00', TRUE),
(9, 18, '2025-05-27 13:30:00', FALSE),
(10, 20, '2025-05-30 16:00:00', TRUE);                                                                               
 --  DROP database buenosasesores;
 -- procedimiento de almacenamiento
 /* registrar un nuevo asesor y verifica que no hayan nombres repertidos */
DELIMITER $$

CREATE PROCEDURE REGISTROASESOR(
    IN p_nombre VARCHAR(255), 
    IN p_email VARCHAR(255),
    IN p_contrasenia VARCHAR(255),
    IN p_nombre_usuario VARCHAR(255),
    IN p_tarifa FLOAT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM ASESOR WHERE nombre_usuario = p_nombre_usuario) THEN
        INSERT INTO ASESOR (nombre, email, contrasenia, nombre_usuario, tarifa)
        VALUES (p_nombre, p_email, p_contrasenia, p_nombre_usuario, p_tarifa);
    ELSE
        SELECT CONCAT('El asesor ', p_nombre_usuario, ' ya existe, no se insertó') AS mensaje;
    END IF;
END$$

CREATE PROCEDURE REGISTROASESORADO(
    IN p_nombre VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_contrasenia VARCHAR(255),
    IN p_nombre_usuario VARCHAR(255)
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM ASESORADO WHERE nombre_usuario = p_nombre_usuario) THEN
        INSERT INTO ASESORADO (nombre, email, contrasenia, nombre_usuario)
        VALUES (p_nombre, p_email, p_contrasenia, p_nombre_usuario);
    ELSE
        SELECT CONCAT('El asesorado ', p_nombre_usuario, ' ya existe, no se insertó') AS mensaje;
    END IF;
END$$

DELIMITER ;
DELIMITER $$

CREATE PROCEDURE AGENDARASESORIA2(
    IN ID_ASESOR INT, 
    IN ID_ASESORADO INT,  -- Cambiar ID_TEMA por ID_ASESORADO
    IN FECHA DATETIME
)
BEGIN
    -- Esta validación ya no es necesaria si no estás verificando temas
    INSERT INTO ASESORIA (id_asesor, id_asesorado, fecha, confirmada)
    VALUES (ID_ASESOR, ID_ASESORADO, FECHA, FALSE);
END $$

DELIMITER ;
CALL AGENDARASESORIA2(1, 1, '2024-01-15 10:00:00');
CALL REGISTROASESOR('Dra. Valentina Fuentes', 'valentina.fuentes@consultor.com', 'passVal2024', 'vfuentes', 85.50);
CALL REGISTROASESORADO('Javier Rodríguez Soto', 'javier.rodriguez@alumno.com', 'jrodriguez2024', 'jrodriguez');
 
CALL REGISTROASESOR('Dra. Wendy Perez', 'wendy40@consultor.com', '12342024', '9ukfpo', 97.50);
CALL REGISTROASESORADO('ediisigler', 'eddi@alumno.com', '58dbws', 'jutnd');
CALL AGENDARASESORIA2(1, 2, '2024-02-15 15:00:00');


call AGENDARASESORIA2(1,1,now())