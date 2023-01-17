-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: smartstore
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `jaelyo`
--

DROP TABLE IF EXISTS `jaelyo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jaelyo` (
  `RECIPE_CODE` text,
  `RECIPE_NAME` text,
  `BASE_GRAM` text,
  `GRAM_PRICE` double DEFAULT NULL,
  `INVENTORY` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jaelyo`
--

LOCK TABLES `jaelyo` WRITE;
/*!40000 ALTER TABLE `jaelyo` DISABLE KEYS */;
INSERT INTO `jaelyo` VALUES ('r1','떡볶이떡','1g',1.8,2000),('r2','대파','1g',3.2,2000),('r3','설탕','1g',1.31,3000),('r4','간장','1g',1.38,1800),('r5','고추장','1g',14.7,14000),('r6','고추가루','1g',11,1000),('r7','양파','1g',2.38,5000),('r8','다진마늘','1g',2.38,1000),('r9','김치','1g',1.23,10000),('r10','돼지고기','1g',8.4,5000),('r11','청양고추','1g',6.9,1000),('r12','체다치즈','1g',10.845,2000),('r13','카레가루','1g',5,1000),('r14','비엔나소세지','1g',6.3,1000),('r15','어묵','1g',4.338,3000),('r16','우유','1ml',2.22,3600),('r17','파마산치즈가루','1g',9,1000),('r18','쌀','1g',2.29,10000),('r19','양배추','1g',3.9,3000),('r20','당근','1g',3.3,3000),('r21','표고버섯','1g',7.4,1000),('r22','숙주','1g',6.3,3000),('r23','새우','1g',13,1000),('r24','참치액젓','1ml',6,900),('r25','야끼소바 소스','1g',13,300),('r26','우동사리면','1g',5.14,2100),('r27','스파게티면','1g',2.7,5000),('r28','올리브오일','1ml	',12.7,1000),('r29','바지락','1g',4.5,1000),('r30','통마늘','1g',7.9,5000),('r31','페페로치노','1g',110,100),('r32','화이트와인','1g',37.5,400),('r33','순두부','1g',6,1000),('r34','애호박','1g',4,1050),('r35','소금','1g',1.9,1000),('r36','후추','1g',20,1000),('r37','식용유','1g',3.6,1000),('r38','고추참치','1g',15,1000);
/*!40000 ALTER TABLE `jaelyo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-17 10:00:18
