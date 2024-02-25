-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
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
('f6dc88ae9e6e');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES
('017f8b11-4e1e-470d-b8f8-38f35d3996c8',8,'734c5844-7cba-4c51-8d0c-9830d09bb562','0af0ada5-057f-4955-a589-8e945c3e0d7b','車のメンテナンス','2024-01-30','2024-02-10','color8','オイル交換とタイヤチェック'),
('05236ffd-eefd-42b1-a895-b474c243316d',4,'7414208f-560c-4641-8d08-f7ea576d4f6f','0af0ada5-057f-4955-a589-8e945c3e0d7b','買い物に行く','2024-01-30','2024-01-31','color4','週末の食料品'),
('29207055-e668-40ef-9668-a0a9d35dca3a',5,'734c5844-7cba-4c51-8d0c-9830d09bb562','0af0ada5-057f-4955-a589-8e945c3e0d7b','犬の散歩','2024-01-30','2024-01-31','color5','公園までの長い散歩'),
('32b49316-3525-491b-a2d5-4c38adf72b4d',10,'7414208f-560c-4641-8d08-f7ea576d4f6f','0af0ada5-057f-4955-a589-8e945c3e0d7b','植物に水をやる','2024-01-30','2024-01-31','color10','すべての室内植物'),
('5fa25678-4df3-458b-87a8-df45397daba3',1,'76cfdd6b-32d9-4938-9c03-32905e50f7ac','0af0ada5-057f-4955-a589-8e945c3e0d7b','朝ごはんを作る','2024-01-30','2024-01-31','color1','昨日のカレー'),
('7e26623f-2903-4e60-b146-0075d38e7503',3,'76cfdd6b-32d9-4938-9c03-32905e50f7ac','0af0ada5-057f-4955-a589-8e945c3e0d7b','ジムに行く','2024-01-30','2024-01-31','color3','新しいトレーニングプランを試す'),
('9ad92ac4-0e74-454f-9b6f-540df58a3e52',7,'7414208f-560c-4641-8d08-f7ea576d4f6f','0af0ada5-057f-4955-a589-8e945c3e0d7b','図書館から本を返す','2024-01-30','2024-01-31','color7','借りていた小説'),
('9c16f9d6-b968-4873-be2e-b30779228211',6,'76cfdd6b-32d9-4938-9c03-32905e50f7ac','0af0ada5-057f-4955-a589-8e945c3e0d7b','友人との会食','2024-01-30','2024-02-03','color6','新しいレストランでのディナー'),
('ae7004f1-eb7c-49bd-b366-83f3ce842568',9,'76cfdd6b-32d9-4938-9c03-32905e50f7ac','0af0ada5-057f-4955-a589-8e945c3e0d7b','家の掃除','2024-01-30','2024-02-01','color9','リビングとキッチン'),
('b2c04f39-66d7-4eaf-af36-d52a23492e94',2,'734c5844-7cba-4c51-8d0c-9830d09bb562','0af0ada5-057f-4955-a589-8e945c3e0d7b','レポートを書く','2024-01-30','2024-02-05','color2','市場分析に関するレポート');
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES
('734c5844-7cba-4c51-8d0c-9830d09bb562',2,'0af0ada5-057f-4955-a589-8e945c3e0d7b','進行中','現在進行中'),
('7414208f-560c-4641-8d08-f7ea576d4f6f',3,'0af0ada5-057f-4955-a589-8e945c3e0d7b','完了','完了しました'),
('76cfdd6b-32d9-4938-9c03-32905e50f7ac',1,'0af0ada5-057f-4955-a589-8e945c3e0d7b','未着手','まだ手を付けていないもの'),
('bf7e0b03-ecd8-415a-8f6b-36ae8c4154ed',4,'0af0ada5-057f-4955-a589-8e945c3e0d7b','未分類','まだよくわからない');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `channels`
--

LOCK TABLES `channels` WRITE;
/*!40000 ALTER TABLE `channels` DISABLE KEYS */;
/*!40000 ALTER TABLE `channels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
('0af0ada5-057f-4955-a589-8e945c3e0d7b','hoge@gmail.com','hogehoge','$2b$12$PAwXKpbmR4BJQJuti8k44OJiHH8M9Yg4vOWg6OVqYOVMLVOr3VXl6');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-25  0:27:42
