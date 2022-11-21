-- MySQL dump 10.13  Distrib 5.5.62, for Linux (x86_64)
--
-- Host: localhost    Database: takeaway
-- ------------------------------------------------------
-- Server version	5.5.62-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food` (
  `food_id` int(11) NOT NULL AUTO_INCREMENT,
  `food_name` varchar(100) DEFAULT NULL,
  `food_price` decimal(10,2) DEFAULT NULL,
  `food_url` varchar(500) DEFAULT NULL,
  `food_type` varchar(100) DEFAULT NULL,
  `store_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`food_id`),
  KEY `store_id` (`store_id`),
  CONSTRAINT `food_ibfk_1` FOREIGN KEY (`store_id`) REFERENCES `store` (`store_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES (2,'酱牛肉盖饭',40.00,'https://wx3.sinaimg.cn/thumb180/007a4Omfgy1fydcx9wk2qj30ec0ff3zp.jpg',NULL,1),(3,'寿司',50.00,'https://wx3.sinaimg.cn/bmiddle/b922c842gy1gxa9fqvgyoj23402c0kjm.jpg',NULL,2),(4,'甜点',20.00,'https://wx1.sinaimg.cn/thumb180/6d29c261gy1gxa96ytq9yj20r70ken1k.jpg','甜品',3),(5,'扇贝',60.00,'https://wx3.sinaimg.cn/thumb180/87156585ly1gwksxbvna5j22qk21xhdu.jpg','海鲜',2),(6,'大闸蟹',55.00,'https://wx3.sinaimg.cn/thumb180/a676fba1gy1gxa5kbxlwoj23402c0hdu.jpg','海鲜',2),(7,'虾饼',30.00,'https://wx3.sinaimg.cn/thumb180/006WATG4ly1gxaatx1itkj30ww1dcamc.jpg',NULL,2),(8,'冷面',10.00,'https://wx1.sinaimg.cn/thumb180/87819c37ly1gxa0ea254aj218g0u0dr4.jpg','韩式',3),(9,'炸鸡',22.00,'https://wx1.sinaimg.cn/thumb180/dd736faaly1gxa72s32a0j211n0u0doh.jpg','韩式',3),(10,'蛋卷',10.00,'https://ww2.sinaimg.cn/thumb180/a4b620d1gw1f4kbn69uxcj20gl0cfjul.jpg',NULL,1),(11,'小炒肉',20.00,'https://wx1.sinaimg.cn/thumb180/7873ea25ly1gx8wvxmrw1j20u00u045e.jpg','家常菜',4),(12,'麻婆豆腐',18.00,'https://wx2.sinaimg.cn/thumb180/62df2d30ly8gxa4ppf2tij20j60csta1.jpg','家常菜',4),(13,'酸辣土豆丝',12.00,'https://wx4.sinaimg.cn/thumb180/968c99ccly1gx9vwyd0h9j20go0ch0tn.jpg','家常菜',4),(14,'鱼香茄子',20.00,'https://wx2.sinaimg.cn/thumb180/005G7cdcly8gx2va7iw05j30c50cdq5k.jpg','家常菜',4),(15,'油麦菜',10.00,'https://wx1.sinaimg.cn/thumb180/006WIDKvly1gx2oh9pawgj30go0m8q57.jpg','家常菜',4),(16,'全家桶',88.00,'https://img0.baidu.com/it/u=783593403,4142964864&fm=26&fmt=auto','快餐',5),(17,'K记饭桶',38.00,'https://img1.baidu.com/it/u=417215786,650247609&fm=26&fmt=auto','快餐',5),(18,'双拼炸鸡',40.00,'https://wx3.sinaimg.cn/thumb180/00603y0Mly1gxa7zc4beuj30n01dstot.jpg','快餐',5);
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_evaluate`
--

DROP TABLE IF EXISTS `food_evaluate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_evaluate` (
  `food_evaluate_id` int(11) NOT NULL AUTO_INCREMENT,
  `food_evaluate_text` varchar(100) DEFAULT NULL,
  `food_evaluate_score` int(11) DEFAULT NULL,
  `food_id` int(11) DEFAULT NULL,
  `post_user_id` int(11) NOT NULL,
  `food_evaluate_date` datetime DEFAULT NULL,
  PRIMARY KEY (`food_evaluate_id`),
  KEY `food_id` (`food_id`),
  KEY `post_user_id` (`post_user_id`),
  CONSTRAINT `food_evaluate_ibfk_1` FOREIGN KEY (`food_id`) REFERENCES `food` (`food_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `food_evaluate_ibfk_2` FOREIGN KEY (`post_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_evaluate`
--

LOCK TABLES `food_evaluate` WRITE;
/*!40000 ALTER TABLE `food_evaluate` DISABLE KEYS */;
INSERT INTO `food_evaluate` VALUES (6,'好吃',5,10,2,'2021-12-05 14:35:49'),(7,'不错',5,4,2,'2021-12-05 14:44:23'),(9,'',5,5,2,'2021-12-05 06:50:55'),(10,'整挺好',4,3,1,'2021-12-05 06:51:56'),(12,'',5,3,2,'2021-12-05 07:04:44'),(16,'?',1,10,1,'2021-12-06 07:09:28'),(18,'',0,10,6,'2021-12-06 13:44:31'),(19,'',1,10,6,'2021-12-06 13:44:32'),(20,'',3,4,8,'2021-12-06 13:57:46'),(21,'',4,4,8,'2021-12-06 13:57:47'),(22,'我爱酸辣土豆丝！',5,13,2,'2021-12-07 05:16:41'),(23,'',3,10,1,'2021-12-07 05:50:40'),(24,'good',4,10,1,'2021-12-07 06:45:31'),(25,'牛逼！！！',5,2,1,'2021-12-07 06:49:00'),(27,'good',4,10,1,'2021-12-07 07:01:26'),(28,'haha',5,2,1,'2021-12-07 09:12:31'),(29,'不好吃，过敏了',2,5,1,'2021-12-07 13:03:30'),(30,'做得很棒，很美味。',5,10,10,'2021-12-09 09:26:34'),(31,'好吃',5,2,11,'2021-12-09 16:47:51'),(33,'zhen haochi',5,2,1,'2021-12-11 08:02:40'),(34,'zhen haochi',5,2,1,'2021-12-11 08:02:48'),(35,'.牛逼周子航牛逼',0,11,1,'2021-12-11 13:16:42'),(36,'回来',4,10,1,'2021-12-11 13:40:03'),(37,'',4,10,1,'2021-12-11 13:40:25'),(38,'测试test\n',3,11,21,'2021-12-11 14:37:39'),(39,'还可以',4,3,1,'2021-12-11 15:52:42'),(40,'真好吃',4,4,1,'2021-12-11 16:36:48'),(41,'真棒',1,10,1,'2021-12-11 17:12:23'),(42,'真棒',1,10,1,'2021-12-11 17:12:28'),(43,'还行',1,2,1,'2021-12-11 17:14:36'),(45,'gggg',5,7,1,'2021-12-12 02:56:38'),(46,'ggggd',5,7,1,'2021-12-12 02:56:43'),(47,'sgbs',5,7,1,'2021-12-12 02:56:53'),(48,'sgshshnsns',5,7,1,'2021-12-12 02:57:01'),(49,'sgshshnsnssnsn',5,7,1,'2021-12-12 02:57:04'),(50,'sgshshnsnssnsn',5,7,1,'2021-12-12 02:57:06'),(51,'sgshshnsnssnsn',5,7,1,'2021-12-12 02:57:08'),(52,'wyxnd',5,7,1,'2021-12-12 02:57:16'),(53,'fff',1,10,1,'2021-12-12 03:05:39'),(54,'fff',1,10,1,'2021-12-12 03:05:43'),(55,'ffff',3,16,1,'2021-12-12 03:07:42'),(56,'不错哦',0,2,23,'2021-12-12 08:01:02'),(57,'haochi',1,10,1,'2021-12-12 08:16:05'),(58,'haochi',1,16,1,'2021-12-12 08:31:15'),(59,'niubi',1,10,1,'2021-12-12 08:38:10'),(60,'niubi',1,16,1,'2021-12-12 08:42:26'),(61,'好吃！',5,17,1,'2021-12-12 09:10:21'),(62,'dbbxjx',4,10,1,'2021-12-12 10:31:09'),(63,'dbbxjx',4,10,1,'2021-12-12 10:31:31'),(64,'',3,16,2,'2021-12-12 14:32:53'),(65,'不错',5,10,2,'2021-12-12 14:54:59'),(66,'真好吃',5,10,2,'2021-12-12 14:55:05'),(67,'牛的',5,2,2,'2021-12-12 15:00:05'),(68,'好吃！',5,2,2,'2021-12-12 15:00:11'),(69,'我觉得很好吃',5,11,2,'2021-12-12 15:01:08'),(70,'为什么人那么多，太无语了',1,16,2,'2021-12-12 15:01:41'),(71,'',5,11,1,'2021-12-13 11:42:45'),(72,'牛逼',4,11,1,'2021-12-14 01:00:23'),(73,'hh',1,10,1,'2021-12-15 08:16:45');
/*!40000 ALTER TABLE `food_evaluate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_completed` tinyint(1) NOT NULL DEFAULT '0',
  `order_user_id` int(11) NOT NULL,
  `delivery_user_id` int(11) DEFAULT NULL,
  `order_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`),
  KEY `order_user_id` (`order_user_id`),
  KEY `delivery_user_id` (`delivery_user_id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`order_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`delivery_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (4,2,1,1,'2021-12-02 12:47:22'),(5,2,1,2,'2021-12-02 12:47:51'),(8,2,1,1,'2021-12-04 09:19:57'),(9,2,1,1,'2021-12-04 09:31:36'),(10,1,2,1,'2021-12-04 17:25:36'),(11,2,2,1,'2021-12-04 09:55:33'),(12,2,1,2,'2021-12-04 22:58:29'),(15,2,1,1,'2021-12-05 06:52:45'),(16,1,2,1,'2021-12-05 06:55:29'),(18,2,1,1,'2021-12-05 09:15:14'),(19,2,1,11,'2021-12-05 09:26:18'),(20,2,6,1,'2021-12-06 05:44:38'),(21,1,8,1,'2021-12-06 05:58:05'),(22,2,1,1,'2021-12-06 22:52:00'),(23,1,2,1,'2021-12-07 04:18:26'),(24,2,1,1,'2021-12-07 04:41:05'),(25,2,1,1,'2021-12-07 05:02:45'),(26,2,1,2,'2021-12-09 03:42:51'),(27,1,11,4,'2021-12-09 08:45:44'),(28,2,1,1,'2021-12-10 16:37:25'),(29,2,1,4,'2021-12-11 00:04:00'),(30,2,1,1,'2021-12-11 05:16:54'),(31,2,1,1,'2021-12-11 05:16:57'),(32,2,1,1,'2021-12-11 05:16:58'),(33,2,1,1,'2021-12-11 05:16:59'),(34,2,1,1,'2021-12-11 05:17:00'),(35,2,1,1,'2021-12-11 05:17:01'),(36,2,1,1,'2021-12-11 05:17:01'),(37,2,1,1,'2021-12-11 05:17:02'),(38,1,21,1,'2021-12-11 06:36:36'),(39,1,1,1,'2021-12-11 15:30:07'),(41,1,1,1,'2021-12-11 15:52:51'),(42,2,1,1,'2021-12-11 15:52:54'),(43,2,1,1,'2021-12-11 16:27:35'),(44,2,1,1,'2021-12-11 17:12:42'),(45,1,1,1,'2021-12-12 02:54:32'),(46,2,1,1,'2021-12-12 02:54:39'),(47,2,1,1,'2021-12-12 03:08:08'),(48,1,1,1,'2021-12-12 03:35:14'),(49,1,1,1,'2021-12-12 08:15:56'),(50,1,1,1,'2021-12-12 08:16:19'),(51,1,1,1,'2021-12-12 08:30:53'),(52,0,1,NULL,'2021-12-12 08:38:02'),(53,0,1,NULL,'2021-12-12 08:38:52'),(54,0,1,NULL,'2021-12-12 08:42:12'),(55,0,1,NULL,'2021-12-12 08:42:42'),(56,0,1,NULL,'2021-12-12 09:09:41'),(57,0,1,NULL,'2021-12-12 14:27:56'),(59,0,1,NULL,'2021-12-14 00:58:23'),(60,0,1,NULL,'2021-12-14 12:02:08'),(61,0,1,NULL,'2021-12-14 12:02:14'),(62,0,1,NULL,'2022-01-18 07:23:26'),(63,0,1,NULL,'2022-01-18 07:23:32');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_food`
--

DROP TABLE IF EXISTS `order_food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_food` (
  `order_food_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `food_id` int(11) DEFAULT NULL,
  `food_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_food_id`),
  KEY `order_id` (`order_id`),
  KEY `food_id` (`food_id`),
  CONSTRAINT `order_food_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `order_food_ibfk_2` FOREIGN KEY (`food_id`) REFERENCES `food` (`food_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_food`
--

LOCK TABLES `order_food` WRITE;
/*!40000 ALTER TABLE `order_food` DISABLE KEYS */;
INSERT INTO `order_food` VALUES (3,4,6,2),(4,4,4,1),(5,5,7,1),(8,8,2,2),(9,9,8,1),(10,10,3,4),(11,10,5,1),(12,10,6,1),(13,10,7,1),(14,11,2,2),(15,11,10,2),(16,12,2,1),(17,12,10,2),(18,15,11,1),(19,15,13,1),(20,16,11,2),(21,16,15,1),(22,18,3,1),(23,18,5,1),(24,18,5,1),(25,19,4,1),(26,19,4,1),(27,19,8,1),(28,19,9,1),(29,19,9,1),(30,19,9,1),(31,20,2,1),(32,20,10,1),(33,20,10,1),(34,21,4,1),(35,21,4,1),(36,21,8,1),(37,21,9,1),(38,22,2,3),(39,22,10,2),(40,23,11,2),(41,23,12,2),(42,23,13,2),(43,23,14,1),(44,23,15,2),(45,24,2,1),(46,24,10,1),(47,24,10,1),(48,25,2,1),(49,25,10,2),(50,26,2,1),(51,26,10,2),(52,27,6,1),(53,28,2,1),(54,29,2,1),(55,29,2,1),(56,29,10,1),(57,30,11,1),(58,31,11,1),(59,32,11,1),(60,33,11,1),(61,34,11,1),(62,35,11,1),(63,36,11,1),(64,37,11,1),(65,38,5,1),(66,38,6,2),(67,38,7,3),(68,39,2,1),(70,41,3,1),(71,42,3,1),(72,43,16,1),(73,43,17,1),(74,44,10,1),(75,45,16,1),(76,46,16,1),(77,47,16,1),(78,48,16,1),(79,48,16,1),(80,49,10,1),(81,50,16,1),(82,51,10,1),(83,52,10,1),(84,53,11,1),(85,54,10,1),(86,55,12,1),(87,56,11,3),(88,56,12,2),(89,56,15,1),(90,57,2,2),(92,59,16,3),(93,59,17,2),(94,59,18,1),(95,60,16,1),(96,60,16,1),(97,60,17,1),(98,62,18,1),(99,63,18,1);
/*!40000 ALTER TABLE `order_food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `star`
--

DROP TABLE IF EXISTS `star`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `star` (
  `star_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`star_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `star_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `star`
--

LOCK TABLES `star` WRITE;
/*!40000 ALTER TABLE `star` DISABLE KEYS */;
INSERT INTO `star` VALUES (4,NULL),(1,1),(2,2),(3,6),(5,11),(6,21);
/*!40000 ALTER TABLE `star` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `star_food`
--

DROP TABLE IF EXISTS `star_food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `star_food` (
  `star_food_id` int(11) NOT NULL AUTO_INCREMENT,
  `star_id` int(11) DEFAULT NULL,
  `food_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`star_food_id`),
  KEY `star_id` (`star_id`),
  KEY `food_id` (`food_id`),
  CONSTRAINT `star_food_ibfk_1` FOREIGN KEY (`star_id`) REFERENCES `star` (`star_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `star_food_ibfk_2` FOREIGN KEY (`food_id`) REFERENCES `food` (`food_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `star_food`
--

LOCK TABLES `star_food` WRITE;
/*!40000 ALTER TABLE `star_food` DISABLE KEYS */;
INSERT INTO `star_food` VALUES (10,2,10),(11,2,5),(33,3,8),(35,2,4),(36,5,2),(40,6,2),(41,6,10),(42,6,11),(43,1,4),(51,1,10),(52,1,11),(53,1,2);
/*!40000 ALTER TABLE `star_food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `store` (
  `store_id` int(11) NOT NULL AUTO_INCREMENT,
  `store_name` varchar(100) DEFAULT NULL,
  `store_address` varchar(100) DEFAULT NULL,
  `store_tel` varchar(100) DEFAULT NULL,
  `store_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES (1,'阳间大饭店','阳间','15518239898','https://gimg2.baidu.com/image_search/src=http%3A%2F%2Ffile2.rrxh5.cc%2Fg2%2Fc1%2F2019%2F10%2F25%2F1571971484383.jpg&refer=http%3A%2F%2Ffile2.rrxh5.cc&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641184718&t=b47a79a61a289119743a6d91a01c7248'),(2,'韩式小餐','阴间','19812893198','https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimage.thepaper.cn%2Fwww%2Fimage%2F9%2F996%2F866.jpg&refer=http%3A%2F%2Fimage.thepaper.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641184763&t=aba6748e68786617b3dd05855caeaeaf'),(3,'642饭店','15公寓642','13940992222','https://img1.baidu.com/it/u=2363013192,3770096151&fm=15&fmt=auto'),(4,'前辈家的小炒菜','前辈家','13999821738','https://static.cn486.com/uploadfile/2021/1011/163393546439236.jpg'),(5,'疯狂星期四','KFC','139182938989','https://img0.baidu.com/it/u=4039828514,218062239&fm=26&fmt=auto');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_nickname` varchar(100) DEFAULT NULL,
  `user_address` varchar(100) NOT NULL,
  `user_tel` varchar(100) NOT NULL,
  `user_icon_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'zzh','pbkdf2_sha256$260000$9nWwzBNSHZ4NUbpQ34QDcp$0zsI6bKQok5O6+BvetcgyrCxRwlrBhttC1QN/hZClcc=','粥童帆','学院路-15公寓','18800130501','http://pic.mcatk.com/soto-pictures/2021-12/psTkdy.jpg'),(2,'charlot','pbkdf2_sha256$260000$aFbsx49mui99DBgieSliNa$b5cZho5GBfp6HC4sFCzUjBlcmu/zlpYlQWRMGfs7zSg=','查洛特','学院路-15公寓','15224018918','https://tva1.sinaimg.cn/large/008i3skNly1gwt39jx9trj30dt0dt408.jpg'),(4,'qlh','pbkdf2_sha256$260000$pFhLEsIhum6q3KUnAKXdiy$9wYNBJkeNUtqwaz/H6P1mC2TAm4TCSWzJ+rfHxn5G/w=','qlh','学院路-15公寓','123','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(5,'wyx','wyx','十年不洗脚','15公寓','123456789103','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(6,'cyj','cyj',NULL,'15','12345678901','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(7,'qlh1','qlh',NULL,'15','12345678902','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(8,'cyj1','cyj','peppermint','dorm15','12345677891','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(10,'zzk','zzk','Kyaru','学院路-15公寓','012345678901','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(11,'zhy','123','eden','学院路-15公寓','11','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(21,'test','pbkdf2_sha256$260000$hXHjn0daTDCbVTakLcF0bi$IEywGSDraBabyuXSI5L404zxr1XzXlw27Tbd78ZsiQs=','Test','学院路-15公寓','123','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(23,'qll','pbkdf2_sha256$260000$XN9cxHSCCs3A3Z1BcWWJmM$JnmRkrzkhlokT0dtofYoRgwIqVinZJuzeI61hZ2hsjo=',NULL,'123@qq.com','110','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(25,'kairetian','pbkdf2_sha256$260000$PhiaWkoaA7uhtgLt3enmUV$BpxpObzt677PyXCYWZ8mME+1HU5KGhwd/BgHN7Z/o1A=',NULL,'ggggg','ggggg','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(26,'','pbkdf2_sha256$260000$6PZo96GNhew6WYFc109SCW$caoIITl0I0WdJa6uON6pQPYoXPZF1kjKz+8gHskPLto=',NULL,'','','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(27,'name','pbkdf2_sha256$260000$8CyWaGPbCUt9dXpIoneJsz$flmOGgQBhTh+imyur6NFFUOvZo9NSNwL2fa6iw5+JaU=',NULL,'haiguxiaohao@163.com','gggggg','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto'),(28,'邱','pbkdf2_sha256$260000$TjfE8YE3X6a2nw6Dh635vc$7k4r7tBAjRX9Dx3SFoYnrzEuDGeVR/MgZYJdfgp0ukM=',NULL,'大运村','153','https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_evaluate`
--

DROP TABLE IF EXISTS `user_evaluate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_evaluate` (
  `user_evaluate_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_evaluate_text` varchar(100) DEFAULT NULL,
  `user_evaluate_score` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `post_user_id` int(11) NOT NULL,
  `user_evaluate_date` datetime DEFAULT NULL,
  PRIMARY KEY (`user_evaluate_id`),
  KEY `user_id` (`user_id`),
  KEY `post_user_id` (`post_user_id`),
  CONSTRAINT `user_evaluate_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_evaluate_ibfk_2` FOREIGN KEY (`post_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_evaluate`
--

LOCK TABLES `user_evaluate` WRITE;
/*!40000 ALTER TABLE `user_evaluate` DISABLE KEYS */;
INSERT INTO `user_evaluate` VALUES (3,'真不错',5,2,1,'2021-12-05 06:48:15'),(4,'真不错',5,1,2,'2021-12-05 06:50:17'),(5,'太棒了',5,1,2,'2021-12-12 14:54:42'),(6,'牛的',5,2,1,'2021-12-13 11:42:27');
/*!40000 ALTER TABLE `user_evaluate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'takeaway'
--

--
-- Dumping routines for database 'takeaway'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-21 16:47:20
