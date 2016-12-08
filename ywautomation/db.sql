-- MySQL dump 10.13  Distrib 5.7.11, for osx10.9 (x86_64)
--
-- Host: localhost    Database: ywautomation_db
-- ------------------------------------------------------
-- Server version	5.7.11

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
-- Current Database: `ywautomation_db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ywautomation_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `ywautomation_db`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `celery_taskmeta`
--

DROP TABLE IF EXISTS `celery_taskmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `celery_taskmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `result` longtext,
  `date_done` datetime NOT NULL,
  `traceback` longtext,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `celery_taskmeta_662f707d` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `celery_tasksetmeta`
--

DROP TABLE IF EXISTS `celery_tasksetmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `celery_tasksetmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) NOT NULL,
  `result` longtext NOT NULL,
  `date_done` datetime NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taskset_id` (`taskset_id`),
  KEY `celery_tasksetmeta_662f707d` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `db_data_info`
--

DROP TABLE IF EXISTS `db_data_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `db_data_info` (
  `db_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `db_name` varchar(50) NOT NULL DEFAULT '' COMMENT 'DB名称',
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `db_type` varchar(20) NOT NULL DEFAULT '' COMMENT 'mysql,redis,mongodb...',
  `db_role` varchar(20) NOT NULL DEFAULT '' COMMENT 'master/slave/date-node/sql-node/...',
  `db_bin_dir` varchar(20) NOT NULL DEFAULT '' COMMENT '数据启动文件及目录',
  `db_data_dir` varchar(50) NOT NULL DEFAULT '' COMMENT '数据库存放目录',
  `db_conf_dir` varchar(50) NOT NULL DEFAULT '' COMMENT 'DB配置文件存放目录',
  `db_port` int(11) NOT NULL DEFAULT '0' COMMENT '数据库端口',
  `defaults_db_name` varchar(50) NOT NULL DEFAULT '' COMMENT '默认数据库name',
  `db_user` varchar(50) NOT NULL DEFAULT '' COMMENT '数据库账号',
  `db_select_pwd` varchar(50) NOT NULL DEFAULT '' COMMENT '数据库查询密码',
  `db_allpri_pwd` varchar(50) NOT NULL DEFAULT '' COMMENT '数据库all密码',
  `content` varchar(1000) NOT NULL DEFAULT '' COMMENT '数据库描述',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`db_id`),
  UNIQUE KEY `db_name` (`db_name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='数据库信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dbautomation_choice`
--

DROP TABLE IF EXISTS `dbautomation_choice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbautomation_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dbautomation_choice_7aa0f6ee` (`question_id`),
  CONSTRAINT `dbautomation_ch_question_id_f7da7935_fk_dbautomation_question_id` FOREIGN KEY (`question_id`) REFERENCES `dbautomation_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dbautomation_question`
--

DROP TABLE IF EXISTS `dbautomation_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbautomation_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` varchar(200) NOT NULL,
  `pub_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_cron_cronjoblog`
--

DROP TABLE IF EXISTS `django_cron_cronjoblog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_cron_cronjoblog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(64) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `is_success` tinyint(1) NOT NULL,
  `message` longtext NOT NULL,
  `ran_at_time` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `django_cron_cronjoblog_code_84da9606_idx` (`code`,`is_success`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_8b50b8fa_idx` (`code`,`start_time`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_4fc78f9d_idx` (`code`,`start_time`),
  KEY `django_cron_cronjoblog_c1336794` (`code`),
  KEY `django_cron_cronjoblog_c4d98dbd` (`start_time`),
  KEY `django_cron_cronjoblog_305d2889` (`end_time`),
  KEY `django_cron_cronjoblog_a05e4b70` (`ran_at_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mytest`
--

DROP TABLE IF EXISTS `mytest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mytest` (
  `id` bigint(20) DEFAULT NULL,
  `c_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `d_time` timestamp NOT NULL DEFAULT '2016-08-01 09:24:44',
  `e_time` timestamp NOT NULL DEFAULT '2016-08-01 09:24:44'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_alarm_port_list`
--

DROP TABLE IF EXISTS `server_alarm_port_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_alarm_port_list` (
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `server_port` int(11) NOT NULL DEFAULT '0' COMMENT '服务器端口',
  `monitor_type` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1 端口监控 2 功能监控 3 状态分析预警',
  `monitor_send_type` varchar(50) NOT NULL DEFAULT '1' COMMENT '1 邮件 2 短信',
  `accept_users` varchar(500) NOT NULL DEFAULT '' COMMENT '接受用户ID，以,分割',
  `alarm_content` varchar(500) NOT NULL DEFAULT '' COMMENT '报警内容',
  `send_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '报警发送时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  KEY `ind_union_id_port` (`server_id`,`server_port`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='服务器端口报警记录列表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_apply_info`
--

DROP TABLE IF EXISTS `server_apply_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_apply_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `project_name` varchar(50) DEFAULT NULL,
  `server_ip` varchar(15) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `server_port` varchar(20) NOT NULL DEFAULT '' COMMENT '服务器ssh端口',
  `apply_type` varchar(200) NOT NULL DEFAULT '' COMMENT '应用类型',
  `apply_name` varchar(100) NOT NULL DEFAULT '' COMMENT '应用名称',
  `apply_port` varchar(20) NOT NULL DEFAULT '' COMMENT '应用端口',
  `apply_tags` varchar(100) NOT NULL DEFAULT '' COMMENT '应用关键字',
  `start_shell_data` varchar(500) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='服务器应用信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_data_info`
--

DROP TABLE IF EXISTS `server_data_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_data_info` (
  `server_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `server_name` varchar(50) NOT NULL DEFAULT '' COMMENT '服务名称',
  `server_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '服务器类型1云机 2物理机器',
  `cpu_data` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'cpu核数',
  `memory_data` tinyint(4) NOT NULL DEFAULT '0' COMMENT '内存大小(G)',
  `func_name` varchar(50) NOT NULL DEFAULT '' COMMENT 'func 名字',
  `group_id` tinyint(4) NOT NULL DEFAULT '0' COMMENT '所属分组id',
  `outer_net` varchar(16) NOT NULL DEFAULT '' COMMENT '外网ip',
  `inner_net` varchar(16) NOT NULL DEFAULT '' COMMENT '内网ip',
  `use_outer_inner` int(11) NOT NULL DEFAULT '2' COMMENT '1 使用内网ip 2 使用外网ip ',
  `ssh_port` int(11) NOT NULL DEFAULT '0' COMMENT 'ssh端口',
  `content` varchar(500) NOT NULL DEFAULT '' COMMENT '机器服务器描述',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`server_id`),
  UNIQUE KEY `server_name` (`server_name`),
  UNIQUE KEY `func_name` (`func_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='服务器信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_port_data`
--

DROP TABLE IF EXISTS `server_monitor_port_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_port_data` (
  `monitor_id` int(11) NOT NULL,
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `server_port` int(11) NOT NULL DEFAULT '0' COMMENT '服务器端口',
  `error_times` tinyint(4) NOT NULL DEFAULT '0' COMMENT '监控正常是0，监控错误随次数＋1',
  `is_report` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 表示为未报警  1 表示已经报警',
  `report_times` tinyint(4) NOT NULL DEFAULT '0' COMMENT '已经报警次数，和server_port_info比较决定是否还需要报警',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`monitor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='服务器端口信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_port_info`
--

DROP TABLE IF EXISTS `server_monitor_port_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_port_info` (
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `server_port` int(11) NOT NULL DEFAULT '0' COMMENT '服务器端口',
  `port_desc` varchar(500) NOT NULL DEFAULT '' COMMENT '端口描述',
  `is_monitor` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否监控 0 否 1 是',
  `error_established_times` tinyint(4) NOT NULL DEFAULT '3' COMMENT '错误确认次数，默认连续3次确认开始报警',
  `serial_report_times` tinyint(4) NOT NULL DEFAULT '3' COMMENT '单次error连续报警次数，默认是3次 ，之后连续有错误也不再报警',
  `is_email_alarm` tinyint(4) NOT NULL DEFAULT '3' COMMENT '是否邮件报警',
  `is_sms_alarm` tinyint(4) NOT NULL DEFAULT '3' COMMENT '是否短信报警',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`server_id`,`server_port`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='服务器端口信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_prototype`
--

DROP TABLE IF EXISTS `server_monitor_prototype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_prototype` (
  `monitor_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'task_id',
  `monitor_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '监控类型 1 mysql 2 redis  3 os 4 port',
  `monitor_target_name` varchar(50) NOT NULL DEFAULT '' COMMENT '监控目标名字,规则:服务器_类型_值类型(num/string)_监控targetname',
  `monitor_target_value` varchar(50) NOT NULL DEFAULT '' COMMENT '监控目标值',
  `monitor_shell` varchar(1000) NOT NULL DEFAULT '' COMMENT '监控shell',
  `is_monitor` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1 监控 0 不监控',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`monitor_id`),
  UNIQUE KEY `uniq_server_monitor_name` (`monitor_type`,`monitor_target_name`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='监控原型列表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_relation`
--

DROP TABLE IF EXISTS `server_monitor_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_relation` (
  `monitor_id` int(11) unsigned NOT NULL,
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `db_id` int(11) NOT NULL DEFAULT '0' COMMENT '数据库id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`monitor_id`,`server_id`,`db_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='监控原型和服务器关系列表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_relation_copy`
--

DROP TABLE IF EXISTS `server_monitor_relation_copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_relation_copy` (
  `monitor_id` int(11) unsigned NOT NULL,
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `db_id` int(11) NOT NULL DEFAULT '0' COMMENT '数据库id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`monitor_id`,`server_id`,`db_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='监控原型和服务器关系列表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_result`
--

DROP TABLE IF EXISTS `server_monitor_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_result` (
  `monitor_id` int(11) NOT NULL DEFAULT '0' COMMENT 'task_id',
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `monitor_values` varchar(200) NOT NULL DEFAULT '' COMMENT '监控值',
  `real_values` varchar(200) NOT NULL DEFAULT '''''',
  `db_id` int(11) NOT NULL DEFAULT '0' COMMENT '数据库id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`monitor_id`,`create_time`,`server_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='数值监控结果表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_result_copy`
--

DROP TABLE IF EXISTS `server_monitor_result_copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_result_copy` (
  `monitor_id` int(11) NOT NULL DEFAULT '0' COMMENT 'task_id',
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `monitor_values` varchar(200) NOT NULL DEFAULT '' COMMENT '监控值',
  `real_values` varchar(200) NOT NULL DEFAULT '''''',
  `db_id` int(11) NOT NULL DEFAULT '0' COMMENT '数据库id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`monitor_id`,`create_time`,`server_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='数值监控结果表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_monitor_result_copy2`
--

DROP TABLE IF EXISTS `server_monitor_result_copy2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_monitor_result_copy2` (
  `monitor_id` int(11) NOT NULL DEFAULT '0' COMMENT 'task_id',
  `server_id` int(11) NOT NULL DEFAULT '0' COMMENT '服务器id',
  `monitor_values` varchar(200) NOT NULL DEFAULT '' COMMENT '监控值',
  `real_values` varchar(200) NOT NULL DEFAULT '''''',
  `db_id` int(11) NOT NULL DEFAULT '0' COMMENT '数据库id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`monitor_id`,`create_time`,`server_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='数值监控结果表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `server_report_monitor_result`
--

DROP TABLE IF EXISTS `server_report_monitor_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_report_monitor_result` (
  `db_id` int(11) NOT NULL,
  `version_values` varchar(100) NOT NULL DEFAULT '' COMMENT '版本信息',
  `mysql_status` varchar(300) NOT NULL DEFAULT '' COMMENT 'mysql状态简要信息',
  `1day_sql_slow` text NOT NULL COMMENT '天慢查询日志',
  `7day_sql_slow` text NOT NULL COMMENT '周慢查询日志',
  `30day_sql_slow` text NOT NULL COMMENT '30天慢查询日志',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `create_time` varchar(10) NOT NULL DEFAULT '2016-01-01' COMMENT '创建时间',
  PRIMARY KEY (`db_id`,`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='mysql－report表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sql_check_task_info`
--

DROP TABLE IF EXISTS `sql_check_task_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sql_check_task_info` (
  `task_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'task_id',
  `check_id` varchar(50) NOT NULL DEFAULT '0' COMMENT '检查id',
  `check_stage` varchar(50) NOT NULL DEFAULT '' COMMENT '这个列显示当前语句已经进行到哪一步了',
  `err_level` varchar(50) NOT NULL DEFAULT '0' COMMENT '0 正常,1表示警告，不影响执行，2表示严重错误，必须修改',
  `stage_status` varchar(50) NOT NULL DEFAULT '' COMMENT '审核成功，则返回 Audit completed,审核失败 返回Execute failed',
  `error_messge` varchar(5000) NOT NULL DEFAULT '' COMMENT '错误内容',
  `check_sql` varchar(1000) NOT NULL DEFAULT '' COMMENT '检查的sql',
  `affected_row` varchar(50) NOT NULL DEFAULT '0' COMMENT '影响的行数',
  `backup_dbname` varchar(50) NOT NULL DEFAULT '' COMMENT '执行结果卸乳数据库',
  `execute_times` varchar(50) NOT NULL DEFAULT '0' COMMENT '执行时间',
  `submit_datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '提交时间',
  `execute_datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '执行时间',
  PRIMARY KEY (`task_id`,`check_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='sqlupdate任务check信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sql_update_task_info`
--

DROP TABLE IF EXISTS `sql_update_task_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sql_update_task_info` (
  `task_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'task_id',
  `user_id` varchar(50) NOT NULL DEFAULT '' COMMENT '用户id',
  `task_style` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 mysql更新 1 redis更新',
  `db_id` char(15) NOT NULL DEFAULT '' COMMENT 'db目标id',
  `update_type` char(15) NOT NULL DEFAULT '' COMMENT '更新类型 1 sql 2 文件',
  `is_inception_use` tinyint(4) NOT NULL DEFAULT '0' COMMENT '1 sql 直接更新 2 inception更新',
  `sql_data` varchar(5000) NOT NULL DEFAULT '' COMMENT 'sql内容',
  `sql_url` varchar(500) NOT NULL DEFAULT '' COMMENT 'sql文件存储地址',
  `task_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 待执行 1 执行',
  `execute_user_id` int(11) NOT NULL DEFAULT '0' COMMENT '执行用户id',
  `submit_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'sql文件提交时间',
  `execute_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '执行时间',
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8 COMMENT='sqlupdate任务表信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sql_update_task_result`
--

DROP TABLE IF EXISTS `sql_update_task_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sql_update_task_result` (
  `task_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'task_id',
  `execute_id` varchar(50) NOT NULL DEFAULT '0' COMMENT '结果id',
  `execute_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '执行类型 1 sql直接提交  2 inception执行',
  `check_stage` varchar(50) NOT NULL DEFAULT '' COMMENT '这个列显示当前语句已经进行到哪一步了',
  `err_level` varchar(50) NOT NULL DEFAULT '0' COMMENT '0 正常,1表示警告，不影响执行，2表示严重错误，必须修改',
  `stage_status` varchar(50) NOT NULL DEFAULT '' COMMENT '审核成功，则返回 Audit completed,审核失败 返回Execute failed',
  `error_messge` varchar(5000) NOT NULL DEFAULT '' COMMENT '错误内容',
  `check_sql` varchar(1000) NOT NULL DEFAULT '' COMMENT '检查的sql',
  `affected_row` varchar(50) NOT NULL DEFAULT '0' COMMENT '影响的行数',
  `backup_dbname` varchar(50) NOT NULL DEFAULT '' COMMENT '执行结果卸乳数据库',
  `sql_execute_info` varchar(500) NOT NULL DEFAULT '' COMMENT 'sql直接执行的结果',
  `execute_times` varchar(50) NOT NULL DEFAULT '0' COMMENT '执行时间',
  `submit_datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '提交时间',
  `execute_datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '执行时间',
  PRIMARY KEY (`task_id`,`execute_id`,`execute_type`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='sqlupdate任务execute结果信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_db_relation`
--

DROP TABLE IF EXISTS `user_db_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_db_relation` (
  `user_id` varchar(50) NOT NULL COMMENT '用户id',
  `db_id` varchar(50) NOT NULL DEFAULT '' COMMENT '数据库id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`,`db_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户数据库关系表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `login_name` varchar(50) NOT NULL DEFAULT '' COMMENT '登录账号名称',
  `login_pwd` varchar(32) NOT NULL DEFAULT '' COMMENT '登录密码',
  `user_name` varchar(50) NOT NULL DEFAULT '' COMMENT '用户姓名',
  `user_email` varchar(50) NOT NULL DEFAULT '' COMMENT '用户邮箱',
  `user_mobile` bigint(20) NOT NULL DEFAULT '0' COMMENT '用户手机号码',
  `user_role` tinyint(4) NOT NULL DEFAULT '0' COMMENT '1 管理员 2 用户',
  `user_department` varchar(20) NOT NULL DEFAULT '' COMMENT '用户部门',
  `is_forbid` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否禁止登录0 禁止 1 正常',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `login_name` (`login_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='数据库信息表';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-08 15:45:28
