CREATE DATABASE  IF NOT EXISTS `basegranes` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `basegranes`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: basegranes
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `butacas`
--

DROP TABLE IF EXISTS `butacas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `butacas` (
  `idButaca` varchar(10) NOT NULL,
  `idSala` int NOT NULL,
  `Fila` int NOT NULL,
  `Asiento` int NOT NULL,
  `Estado` varchar(1) NOT NULL,
  PRIMARY KEY (`idButaca`),
  KEY `idSala_idx` (`idSala`),
  CONSTRAINT `iddeSala` FOREIGN KEY (`idSala`) REFERENCES `salas` (`idSala`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `butacas`
--

LOCK TABLES `butacas` WRITE;
/*!40000 ALTER TABLE `butacas` DISABLE KEYS */;
INSERT INTO `butacas` VALUES ('111',11,1,1,'A'),('1110',11,2,10,'A'),('112',11,1,2,'A'),('113',11,1,3,'A'),('114',11,1,4,'A'),('115',11,1,5,'A'),('116',11,1,6,'A'),('117',11,2,7,'A'),('118',11,2,8,'A'),('119',11,2,9,'A'),('121',12,1,1,'A'),('1210',12,2,10,'A'),('122',12,1,2,'A'),('123',12,1,3,'A'),('124',12,1,4,'A'),('125',12,1,5,'A'),('126',12,1,6,'A'),('127',12,1,7,'A'),('128',12,1,8,'A'),('129',12,2,9,'A'),('131',13,1,1,'A'),('1310',13,2,10,'A'),('132',13,1,2,'A'),('133',13,1,3,'A'),('134',13,1,4,'A'),('135',13,1,5,'A'),('136',13,2,6,'A'),('137',13,2,7,'A'),('138',13,2,8,'A'),('139',13,2,9,'A'),('141',14,1,1,'A'),('1410',14,2,10,'A'),('142',14,1,2,'A'),('143',14,1,3,'A'),('144',14,1,4,'A'),('145',14,1,5,'A'),('146',14,2,6,'A'),('147',14,2,7,'A'),('148',14,2,8,'A'),('149',14,2,9,'A');
/*!40000 ALTER TABLE `butacas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clasificacion`
--

DROP TABLE IF EXISTS `clasificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clasificacion` (
  `idClasificacion` int NOT NULL,
  `Clasificacion` varchar(15) NOT NULL,
  PRIMARY KEY (`idClasificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clasificacion`
--

LOCK TABLES `clasificacion` WRITE;
/*!40000 ALTER TABLE `clasificacion` DISABLE KEYS */;
INSERT INTO `clasificacion` VALUES (1,'ATP'),(2,'+13'),(3,'+18');
/*!40000 ALTER TABLE `clasificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `NombreCli` varchar(45) NOT NULL,
  `ApellidoCli` varchar(45) NOT NULL,
  `MailCli` varchar(50) DEFAULT NULL,
  `ClaveCli` varchar(45) DEFAULT NULL,
  `UltTrans` date DEFAULT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `ApeNom` (`ApellidoCli`,`NombreCli`),
  KEY `UltTrans` (`UltTrans`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Andrea','Rodriguez','arodriguez@gmail.com',NULL,'2020-02-19'),(2,'Carlos','Perez','carlos_perez23@yahoo.com',NULL,'2019-12-15'),(3,'Alicia','Lopez','alopez@uol.com',NULL,'2020-03-12'),(4,'Roberto','Carlos','robert_charles@hotmail.com',NULL,'2019-10-08'),(5,'Jose','Rodriguez','jrodriguez@gmail.com',NULL,'2019-08-02'),(6,'Ana','Garcia','anita_garcia88@yahoo.com',NULL,'2020-01-18'),(7,'Maria','Gonzalez','mary_gonzalez@gmail.com',NULL,'2020-01-11'),(8,'Claudio','Martinez','cmartinez@yahoo.com',NULL,'2020-03-03');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `complejos`
--

DROP TABLE IF EXISTS `complejos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `complejos` (
  `idComplejo` int NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Calle` varchar(45) DEFAULT NULL,
  `Numero` int DEFAULT NULL,
  `Localidad` varchar(45) DEFAULT NULL,
  `CodPos` varchar(8) DEFAULT NULL,
  `Pcia` varchar(25) DEFAULT NULL,
  `Telefonos` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idComplejo`),
  KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complejos`
--

LOCK TABLES `complejos` WRITE;
/*!40000 ALTER TABLE `complejos` DISABLE KEYS */;
INSERT INTO `complejos` VALUES (1,'Palermo','Berutti',1233,'C.A.B.A.','C1111DFD','C.A.B.A.','11 4965-2233'),(2,'Caballito','Av. Rivadavia',2334,'C.A.B.A.','M1223DAS','C.A.B.A.','11 4881-1122'),(3,'Avellaneda','Av. Mitre',4500,'Avellaneda','S1870EEV','Buenos Aires','11 4203-8866'),(4,'Almagro','Av. Scalabrini Ortiz',1223,'C.A.B.A.','M1230DHS','C.A.B.A.','11 4771-1234');
/*!40000 ALTER TABLE `complejos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creditcard`
--

DROP TABLE IF EXISTS `creditcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creditcard` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `idCcard` varchar(16) NOT NULL,
  `idCliente` int NOT NULL,
  `CCTitular` varchar(45) NOT NULL,
  `Emisor` varchar(45) NOT NULL,
  `CCVenc` varchar(4) NOT NULL,
  `CCCodSeg` varchar(4) NOT NULL,
  `Estado` varchar(1) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `idCcard_U` (`idCcard`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `FKidClienteCC` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditcard`
--

LOCK TABLES `creditcard` WRITE;
/*!40000 ALTER TABLE `creditcard` DISABLE KEYS */;
INSERT INTO `creditcard` VALUES (1,'1111222233334444',1,'ANDREA LUCIA RODRIGUEZ','AMEX','1021','012','A'),(2,'2233121234442345',2,'CARLOS PEREZ','VISA GALICIA','0822','122','A'),(3,'0123345518922000',3,'ALICIA KARINA LOPEZ','VISA','1220','922','A'),(4,'9090234556781255',4,'ROBERTO CARLOS','VISA ICBC','1219','023','I'),(5,'0112122245660890',5,'JOSE LUIS RODRIGUEZ','AMEX','0321','111','A'),(6,'1100220044000022',6,'ANA GARCIA','MASTER CIUDAD','0821','988','A'),(7,'0012230050609900',7,'MARIA GONZALEZ','VISA','1022','796','A'),(8,'0345456022330110',8,'CLAUDIO O MARTINEZ','VISA GALICIA','1220','100','A');
/*!40000 ALTER TABLE `creditcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formatos`
--

DROP TABLE IF EXISTS `formatos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formatos` (
  `idFormato` int NOT NULL,
  `Formato` varchar(15) NOT NULL,
  PRIMARY KEY (`idFormato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formatos`
--

LOCK TABLES `formatos` WRITE;
/*!40000 ALTER TABLE `formatos` DISABLE KEYS */;
INSERT INTO `formatos` VALUES (1,'2D'),(2,'3D');
/*!40000 ALTER TABLE `formatos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funciones`
--

DROP TABLE IF EXISTS `funciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funciones` (
  `idFuncion` int NOT NULL,
  `idComplejo` int NOT NULL,
  `idSala` int NOT NULL,
  `idPelicula` int NOT NULL,
  `Fecha` date NOT NULL,
  `Horario` time NOT NULL,
  `Valor` decimal(8,2) NOT NULL,
  PRIMARY KEY (`idFuncion`),
  KEY `idPelicula_idx` (`idPelicula`),
  KEY `idSala_idx` (`idSala`),
  CONSTRAINT `idPelicula` FOREIGN KEY (`idPelicula`) REFERENCES `peliculas` (`idPelicula`),
  CONSTRAINT `idSala` FOREIGN KEY (`idSala`) REFERENCES `salas` (`idSala`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funciones`
--

LOCK TABLES `funciones` WRITE;
/*!40000 ALTER TABLE `funciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `funciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generos`
--

DROP TABLE IF EXISTS `generos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generos` (
  `idGenero` int NOT NULL,
  `Genero` varchar(15) NOT NULL,
  PRIMARY KEY (`idGenero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generos`
--

LOCK TABLES `generos` WRITE;
/*!40000 ALTER TABLE `generos` DISABLE KEYS */;
INSERT INTO `generos` VALUES (1,'Ciencia Ficcion'),(2,'Belica'),(3,'Terror'),(4,'Suspenso'),(5,'Drama'),(6,'Comedia'),(7,'Policial'),(8,'Romantica'),(9,'Musical');
/*!40000 ALTER TABLE `generos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peliculas` (
  `idPelicula` int NOT NULL,
  `Titulo` varchar(45) NOT NULL,
  `idGenero` int NOT NULL,
  `Duracion` time NOT NULL,
  `idClasificacion` int NOT NULL,
  `idFormato` int NOT NULL,
  `Idioma` varchar(20) NOT NULL,
  `Director` varchar(45) NOT NULL,
  PRIMARY KEY (`idPelicula`),
  KEY `idGenero_idx` (`idGenero`),
  KEY `idFormato_idx` (`idFormato`),
  KEY `idClasificacion_idx` (`idClasificacion`),
  CONSTRAINT `idClasificacion` FOREIGN KEY (`idClasificacion`) REFERENCES `clasificacion` (`idClasificacion`),
  CONSTRAINT `idFormato` FOREIGN KEY (`idFormato`) REFERENCES `formatos` (`idFormato`),
  CONSTRAINT `idGenero` FOREIGN KEY (`idGenero`) REFERENCES `generos` (`idGenero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
INSERT INTO `peliculas` VALUES (1,'ALIEN',1,'02:00:00',1,1,'CASTELLANO','Ridley Scott'),(2,'TERMINATOR',1,'01:45:00',2,1,'SUBTITULADA','James Cameron'),(3,'PELOTON',2,'02:10:00',3,1,'SUBTITULADA','Oliver Stone'),(4,'IT',3,'03:00:00',3,1,'SUBTITULADA','Andy Muschietti'),(5,'EL EXORCISTA',3,'02:00:00',3,1,'CASTELLANO','William Friedkin'),(6,'TERMINATOR',1,'01:45:00',2,2,'CASTELLANO','James Cameron'),(7,'STAR WARS EPISODIO IV',1,'01:55:00',1,1,'SUBTITULADA','George Lucas'),(8,'STAR WARS EPISODIO V',1,'01:50:00',1,2,'SUBTITULADA','George Lucas'),(9,'STAR WARS EPISODIO VI',1,'02:10:00',1,1,'SUBTITULADA','George Lucas'),(10,'2001 ODISEA DEL ESPACIO',1,'03:10:00',2,1,'SUBTITULADA','Stanley Kubrick'),(11,'TITANIC',5,'02:45:00',2,2,'SUBTITULADA','James Cameron');
/*!40000 ALTER TABLE `peliculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salas`
--

DROP TABLE IF EXISTS `salas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salas` (
  `idSala` int NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Cant Butacas` int NOT NULL,
  `idComplejo` int NOT NULL,
  PRIMARY KEY (`idSala`),
  KEY `idComplejo_idx` (`idComplejo`),
  CONSTRAINT `fk_salas_complejos` FOREIGN KEY (`idComplejo`) REFERENCES `complejos` (`idComplejo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salas`
--

LOCK TABLES `salas` WRITE;
/*!40000 ALTER TABLE `salas` DISABLE KEYS */;
INSERT INTO `salas` VALUES (11,'Sala 1',10,1),(12,'Sala 2',10,1),(13,'Sala 3',10,1),(14,'Sala 4',10,1),(21,'Sala 1',10,2),(22,'Sala 2',10,2),(23,'Sala 3',10,2),(31,'Sala 1',10,3),(32,'Sala 2',10,3),(33,'Sala 3',10,3);
/*!40000 ALTER TABLE `salas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `idTicket` int NOT NULL,
  `idComprobante` varchar(13) NOT NULL,
  `idFuncion` int NOT NULL,
  `idButaca` varchar(10) NOT NULL,
  `Valor` decimal(8,2) NOT NULL,
  PRIMARY KEY (`idTicket`),
  KEY `idComprobante_idx` (`idComprobante`),
  KEY `idFuncion_idx` (`idFuncion`),
  KEY `idButaca_idx` (`idButaca`),
  CONSTRAINT `idButaca` FOREIGN KEY (`idButaca`) REFERENCES `butacas` (`idButaca`),
  CONSTRAINT `idComprobante` FOREIGN KEY (`idComprobante`) REFERENCES `ventascab` (`idComprobante`),
  CONSTRAINT `idFuncion` FOREIGN KEY (`idFuncion`) REFERENCES `funciones` (`idFuncion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventascab`
--

DROP TABLE IF EXISTS `ventascab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventascab` (
  `idComprobante` varchar(13) NOT NULL,
  `idComplejo` int NOT NULL,
  `idCliente` int NOT NULL,
  `Fecha` date NOT NULL,
  `Hora` time NOT NULL,
  `Descuento` decimal(8,2) NOT NULL,
  `Total` decimal(8,2) NOT NULL,
  PRIMARY KEY (`idComprobante`),
  KEY `idComplejo_idx` (`idComplejo`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `fk_ventascab_complejos` FOREIGN KEY (`idComplejo`) REFERENCES `complejos` (`idComplejo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventascab`
--

LOCK TABLES `ventascab` WRITE;
/*!40000 ALTER TABLE `ventascab` DISABLE KEYS */;
/*!40000 ALTER TABLE `ventascab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vmovie`
--

DROP TABLE IF EXISTS `vmovie`;
/*!50001 DROP VIEW IF EXISTS `vmovie`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vmovie` AS SELECT 
 1 AS `idPelicula`,
 1 AS `Titulo`,
 1 AS `Duracion`,
 1 AS `Idioma`,
 1 AS `Director`,
 1 AS `Genero`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'basegranes'
--

--
-- Dumping routines for database 'basegranes'
--

--
-- Final view structure for view `vmovie`
--

/*!50001 DROP VIEW IF EXISTS `vmovie`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vmovie` AS select `p`.`idPelicula` AS `idPelicula`,`p`.`Titulo` AS `Titulo`,`p`.`Duracion` AS `Duracion`,`p`.`Idioma` AS `Idioma`,`p`.`Director` AS `Director`,`g`.`Genero` AS `Genero` from (`peliculas` `p` join `generos` `g` on((`p`.`idGenero` = `g`.`idGenero`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-13 18:27:50
