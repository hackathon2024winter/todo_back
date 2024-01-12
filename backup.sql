-- MariaDB dump 10.19  Distrib 10.11.4-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: mysql_fast    Database: fastapi_todo
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES
('dd2b3d79048b');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `channels`
--

LOCK TABLES `channels` WRITE;
/*!40000 ALTER TABLE `channels` DISABLE KEYS */;
INSERT INTO `channels` VALUES
(1,'830e76f4-2c58-48c1-905e-1367387a693a','ぼっち部屋','hogeさんの孤独な部屋です'),
(2,'d53521e1-2357-45cf-98ba-46d4f887f4ea','サッカー部屋','fugaさんのサッカー部屋です'),
(3,'0c95e2ce-b37c-4dc6-8065-f3594734be2d','宇宙部屋','spaceさんの宇宙部屋です');
/*!40000 ALTER TABLE `channels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES
(1,'830e76f4-2c58-48c1-905e-1367387a693a',1,'誰かかまってください、、','2024-01-12 02:18:50'),
(2,'d53521e1-2357-45cf-98ba-46d4f887f4ea',1,'何か御用で？','2024-01-12 02:20:43'),
(3,'0c95e2ce-b37c-4dc6-8065-f3594734be2d',3,'宇宙世紀が始まります。','2024-01-12 02:30:19'),
(4,'d53521e1-2357-45cf-98ba-46d4f887f4ea',3,'え？マジで？','2024-01-12 02:32:46'),
(5,'d53521e1-2357-45cf-98ba-46d4f887f4ea',2,'京都の原大智に期待','2024-01-12 02:36:17'),
(6,'830e76f4-2c58-48c1-905e-1367387a693a',2,'そう。彼は実に良い。','2024-01-12 02:58:25');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
('0c95e2ce-b37c-4dc6-8065-f3594734be2d','space@gmail.com','space','$2b$12$XNa4.yvzmRvxd.IQQ3DBfOQoPv4EtChANTuwp/FR9FHAFN68d40uC'),
('830e76f4-2c58-48c1-905e-1367387a693a','hoge@gmail.com','hogehoge','$2b$12$OFfPoZIhK8lD8GvvMopB4eO7jDsCT9Ur6Gkr2lO3Y3NYXlNS2UAr2'),
('d53521e1-2357-45cf-98ba-46d4f887f4ea','fuga@gmail.com','fugafuga','$2b$12$1aHBNhS8pQKBqgllaROV..I4ZGjx9.Cp72uvrxU6fjFFBgP4us6Me');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-12 12:03:56
