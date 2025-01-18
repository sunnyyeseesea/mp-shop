/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : sports_shop

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 04/05/2023 00:45:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `says_id` int(0) NOT NULL AUTO_INCREMENT,
  `says_time` date NULL DEFAULT NULL,
  `says` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `goods_id` int(0) NULL DEFAULT NULL,
  `user_id` int(0) NULL DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `order_id` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`says_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES (1, '2024-12-04', '薇我50，肯德基疯狂星期四', 1, 2, '冰镇生鲜', 3);
INSERT INTO `comment` VALUES (2, '2024-12-04', '薇我30，肯德基疯狂星期四', 1, 2, '冰镇生鲜', 3);
INSERT INTO `comment` VALUES (3, '2024-12-05', '薇我20，肯德基疯狂星期四', 1, 2, '冰镇生鲜', 3);
INSERT INTO `comment` VALUES (4, '2024-12-11', '薇我10，肯德基疯狂星期四', 1, 2, '冰镇生鲜', 3);
INSERT INTO `comment` VALUES (5, '2024-12-12', '一个冷静的帅哥来过，并留下一条评论', 6, 1, 'admin', 54);
INSERT INTO `comment` VALUES (6, '2024-12-13', '大苏打实打实的', 2, 1, 'admin', 47);
INSERT INTO `comment` VALUES (7, '2024-12-13', '我是大帅哥', 4, 1, 'admin', 49);
INSERT INTO `comment` VALUES (8, '2024-12-14', '今天天气真不错', 1, 4, '冰镇生鲜', 62);
INSERT INTO `comment` VALUES (9, '2024-12-14', '吃了没', 1, 4, '冰镇生鲜', 63);
INSERT INTO `comment` VALUES (10, '2024-12-14', '薇我50，肯德基疯狂星期四', 1, 2, '冰镇生鲜', 3);
INSERT INTO `comment` VALUES (11, '2024-12-14', '一个冷静的帅哥来过，并留下一条评论', 4, 1, 'admin', 60);
INSERT INTO `comment` VALUES (12, '2024-12-17', 'diapsjdiljad', 2, 1, 'admin', 69);
INSERT INTO `comment` VALUES (13, '2024-12-17', '有点问题', 5, 1, 'admin', 61);
INSERT INTO `comment` VALUES (14, '2024-12-17', '掩饰一下下', 3, 1, 'admin', 74);
INSERT INTO `comment` VALUES (15, '2024-12-17', '倒萨的记录', 4, 1, 'admin', 67);
INSERT INTO `comment` VALUES (16, '2024-12-18', '一个小测试', 1, 1, 'admin', 76);
INSERT INTO `comment` VALUES (17, '2024-12-19', '真不错，运动手表真不错', 5, 1, 'admin', 81);
INSERT INTO `comment` VALUES (18, '2024-04-26', '超级棒，一定要买啊', 2, 3, 'admin', 4);
INSERT INTO `comment` VALUES (19, '2024-04-26', '超级棒，一定要买啊', 2, 3, 'admin', 4);
INSERT INTO `comment` VALUES (20, '2023-04-26', '超级棒，一定要买啊', 2, 3, 'admin', 4);
INSERT INTO `comment` VALUES (21, '2023-04-29', '薇我50，肯德基疯狂星期四', 1, 2, '冰镇生鲜', 3);
INSERT INTO `comment` VALUES (22, '2023-04-29', '一个冷静的帅哥来过，并留下一条评论22233', 4, 1, 'admin', 100);
INSERT INTO `comment` VALUES (23, '2023-04-30', '真不错，我超爱', 1, 1, 'admin', 83);
INSERT INTO `comment` VALUES (24, '2023-04-30', '哎哟不错哦', 2, 1, 'admin', 84);

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `goods_id` int(0) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `goods_price` int(0) NULL DEFAULT NULL,
  `goods_picture` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `goods_describe` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`goods_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES (1, '苹果手表SE', 799, 'http://127.0.0.1:8888/static/picture/applewatchse.jpg', '超值超有料');
INSERT INTO `goods` VALUES (2, 'Series8手表', 4399, 'http://127.0.0.1:8888/static/picture/applewatchSeries8.jpg', '健康的一大步');
INSERT INTO `goods` VALUES (3, '小米手表', 3699, 'http://127.0.0.1:8888/static/picture/xiaomi.jpg', '为发烧而生');
INSERT INTO `goods` VALUES (4, '华为手表', 2699, 'http://127.0.0.1:8888/static/picture/huawei.jpg', '麒麟奶奶提');
INSERT INTO `goods` VALUES (5, '荣耀手表', 1799, 'http://127.0.0.1:8888/static/picture/nonyao.jpg', '遥遥领先遥遥领先');
INSERT INTO `goods` VALUES (6, 'oppo手表', 2399, 'http://127.0.0.1:8888/static/picture/oppo.jpg', '冰川灰，驭雪登场');
INSERT INTO `goods` VALUES (7, '一号', 2.9, 'http://127.0.0.1:8888/static/picture/01.jpg', '冰川灰，驭雪登场');
INSERT INTO `goods` VALUES (8, '二号', 2.9, 'http://127.0.0.1:8888/static/picture/02.jpg', '冰川灰，驭雪登场');
INSERT INTO `goods` VALUES (9, '三号', 2.9, 'http://127.0.0.1:8888/static/picture/03.jpg', '冰川灰，驭雪登场');
INSERT INTO `goods` VALUES (10, '四号', 2.9, 'http://127.0.0.1:8888/static/picture/04.jpg', '冰川灰，驭雪登场');
INSERT INTO `goods` VALUES (11, '五号', 2.9, 'http://127.0.0.1:8888/static/picture/05.jpg', '冰川灰，驭雪登场');
INSERT INTO `goods` VALUES (12, '六号', 2.9, 'http://127.0.0.1:8888/static/picture/06.jpg', '冰川灰，驭雪登场');



-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `order_id` int(0) NOT NULL AUTO_INCREMENT,
  `order_time` datetime(0) NULL DEFAULT NULL,
  `order_count` int(0) NULL DEFAULT NULL,
  `order_amount` int(0) NULL DEFAULT NULL,
  `user_id` int(0) NULL DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `goods_id` int(0) NULL DEFAULT NULL,
  `goods_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `goods_price` int(0) NULL DEFAULT NULL,
  `goods_picture` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `goods_describe` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `says` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`order_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 111 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES (62, '2024-12-14 ', 1, 799, 4, '冰镇生鲜', 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', '今天天气真不错');
INSERT INTO `orders` VALUES (63, '2024-12-14 ', 1, 799, 4, '冰镇生鲜', 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', '吃了没');
INSERT INTO `orders` VALUES (64, '2024-12-14 ', 1, 799, 4, '冰镇生鲜', 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', '买家未做出评价');
INSERT INTO `orders` VALUES (65, '2024-12-14 ', 1, 799, 4, '冰镇生鲜', 1, '红米note', 799, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', NULL);
INSERT INTO `orders` VALUES (66, '2024-12-14 ', 1, 1999, 4, '冰镇生鲜', 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', '买家未做出评价');
INSERT INTO `orders` VALUES (97, '2024-04-29 ', NULL, NULL, NULL, '冰镇生鲜', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `orders` VALUES (98, '2024-04-29', NULL, NULL, NULL, '冰镇生鲜', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `orders` VALUES (99, '2024-04-29 ', NULL, NULL, NULL, '冰镇生鲜', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `orders` VALUES (100, '2024-04-29 ', NULL, NULL, NULL, '冰镇生鲜', NULL, NULL, NULL, NULL, NULL, '一个冷静的帅哥来过，并留下一条评论22233');
INSERT INTO `orders` VALUES (102, '2024-04-29 ', 1, 1999, 4, '冰镇生鲜', 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', NULL);
INSERT INTO `orders` VALUES (103, '2024-04-29 ', 1, 1999, 4, '冰镇生鲜', 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', NULL);
INSERT INTO `orders` VALUES (111, '2024-05-03 ', 1, 4399, 1, 'admin', 2, 'Series8手表', 4399, 'http://127.0.0.1:8888/static/picture/applewatchSeries8.jpg', '健康的一大步', NULL);
INSERT INTO `orders` VALUES (112, '2024-05-03 ', 1, 1799, 1, 'admin', 5, '荣耀手表', 1799, 'http://127.0.0.1:8888/static/picture/nonyao.jpg', '遥遥领先遥遥领先', NULL);
INSERT INTO `orders` VALUES (113, '2024-05-03 ', 1, 2699, 1, 'admin', 4, '华为手表', 2699, 'http://127.0.0.1:8888/static/picture/huawei.jpg', '麒麟奶奶提', NULL);
INSERT INTO `orders` VALUES (114, '2024-05-03 ', 1, 799, 1, 'admin', 1, '苹果手表SE', 799, 'http://127.0.0.1:8888/static/picture/applewatchse.jpg', '超值超有料', NULL);
INSERT INTO `orders` VALUES (115, '2024-05-03 ', 1, 4399, 1, 'admin', 2, 'Series8手表', 4399, 'http://127.0.0.1:8888/static/picture/applewatchSeries8.jpg', '健康的一大步', NULL);
INSERT INTO `orders` VALUES (116, '2024-05-03 ', 1, 2699, 1, 'admin', 4, '华为手表', 2699, 'http://127.0.0.1:8888/static/picture/huawei.jpg', '麒麟奶奶提', NULL);

-- ----------------------------
-- Table structure for shopping_cart
-- ----------------------------
DROP TABLE IF EXISTS `shopping_cart`;
CREATE TABLE `shopping_cart`  (
  `shopping_cart_id` int(0) NOT NULL AUTO_INCREMENT,
  `shopping_count` int(0) NULL DEFAULT NULL,
  `shopping_amount` int(0) NULL DEFAULT NULL,
  `goods_id` int(0) NULL DEFAULT NULL,
  `goods_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `goods_price` int(0) NULL DEFAULT NULL,
  `goods_picture` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `goods_describe` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `user_id` int(0) NULL DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`shopping_cart_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 114 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shopping_cart
-- ----------------------------
INSERT INTO `shopping_cart` VALUES (4, 1, 799, 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', 4, '冰镇生鲜');
INSERT INTO `shopping_cart` VALUES (63, 1, 799, 1, '红米note', 799, 'http://localhost:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', 15, 'root');
INSERT INTO `shopping_cart` VALUES (64, 1, 1999, 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', 4, '冰镇生鲜');
INSERT INTO `shopping_cart` VALUES (88, 1, 4399, 2, 'Series8手表', 4399, 'http://localhost:8888/sports_shop_backend_war/users_picture/applewatchSeries8.jpg', '健康的一大步', 21, 'kang');
INSERT INTO `shopping_cart` VALUES (89, 1, 3699, 3, '小米手表', 3699, 'http://localhost:8888/sports_shop_backend_war/users_picture/xiaomi.jpg', '为发烧而生', 21, 'kang');
INSERT INTO `shopping_cart` VALUES (102, 1, 1999, 1, '红米note', 1999, 'http://192.168.123.53:8888/sports_shop_backend_war/users_picture/kzb68up.jpg', '为发烧而生', 4, '冰镇生鲜');
INSERT INTO `shopping_cart` VALUES (120, 1, 3699, 3, '小米手表', 3699, 'http://127.0.0.1:8888/static/picture/xiaomi.jpg', '为发烧而生', 1, 'admin');
INSERT INTO `shopping_cart` VALUES (121, 1, 2399, 6, 'oppo手表', 2399, 'http://127.0.0.1:8888/static/picture/oppo.jpg', '冰川灰，驭雪登场', 1, 'admin');
INSERT INTO `shopping_cart` VALUES (122, 1, 799, 1, '苹果手表SE', 799, 'http://127.0.0.1:8888/static/picture/applewatchse.jpg', '超值超有料', 1, 'admin');


-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `user_id` int(0) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `level` int(0) NULL DEFAULT NULL,
  `grade` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `wallet` int(0) NULL DEFAULT NULL,
  `user_picture` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `state_message` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'admin', '123456', 1, 'vip', 'root', 2967776, 'http://127.0.0.1:8888/static/picture/kzb68up.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (4, '冰镇生鲜', '123456', 1, 'vip', 'root', -14187, 'http://127.0.0.1:8888/static/picture/kzb68up.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (6, 'kzb', '123456', 1, 'vip', 'root', 1300, 'http://127.0.0.1:8888/static/picture/kzb68up.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (8, '海边的小海鸥', '123456', 1, 'vip', 'normal', 1000, 'http://127.0.0.1:8888/static/picture/user.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (9, '帅哥彬', '123456', 1, 'vip', 'root', 1000, 'http://127.0.0.1:8888/static/picture/风景1.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (10, '海边的小海鸥', '123456', 1, 'vip', 'normal', 1000, 'http://127.0.0.1:8888/static/picture/风景1.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (11, '一个人用鼻毛', '123456', 1, 'vip', 'normal', 1000, 'http://127.0.0.1:8888/static/picture/风景2.jpeg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (15, 'root', '123456', 1, 'vip', 'normal', 1000, 'http://127.0.0.1:8888/static/picture/风景1.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (16, 'kzb', '123456', 1, 'vip', 'root', 1000, 'http://127.0.0.1:8888/static/picture/kzb68up.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (18, 'bin', '123456', 1, 'vip', 'root', 1000, 'http://127.0.0.1:8888/static/picture/风景1.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (21, 'kang', '123456', 1, 'vip', 'root', 1000, 'http://127.0.0.1:8888/static/picture/风景3.jpeg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (22, 'admin', '123', 1, 'vip', 'kk', 100, 'http://127.0.0.1:8888/static/picture/user.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (23, 'admin', '123', 1, 'vip', 'kk', 100, 'http://127.0.0.1:8888/static/picture/user.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (24, 'admin', '123', 1, 'vip', 'kk', 100, 'http://127.0.0.1:8888/static/picture/user.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (25, 'kzb', '123456', 1, 'vip', 'root', 1000, 'http://127.0.0.1:8888/static/picture/kzb68up.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (26, 'kzb', '123456', 1, 'vip', 'root', 1000, 'http://127.0.0.1:8888/static/picture/kzb68up.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (27, 'kzb', '123456', 1, 'vip', 'root', 1000, 'http://127.0.0.1:8888/static/picture/kzb68up.jpg', '这个人很懒，什么都没有留下');
INSERT INTO `users` VALUES (28, 'handsome', '123456', 1, 'vip', 'normal', 1000, 'http://127.0.0.1:8888/static/picture/R.jpg', '这个人很懒，什么都没有留下');

SET FOREIGN_KEY_CHECKS = 1;
