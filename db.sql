SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `barnyard` DEFAULT CHARACTER SET latin1 ;
USE `barnyard` ;

-- -----------------------------------------------------
-- Table `barnyard`.`data`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`data` (
  `sid` INT(10) UNSIGNED NOT NULL ,
  `cid` INT(10) UNSIGNED NOT NULL ,
  `data_payload` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`sid`, `cid`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`detail`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`detail` (
  `detail_type` TINYINT(3) UNSIGNED NOT NULL ,
  `detail_text` TEXT NOT NULL ,
  PRIMARY KEY (`detail_type`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`encoding`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`encoding` (
  `encoding_type` TINYINT(3) UNSIGNED NOT NULL ,
  `encoding_text` TEXT NOT NULL ,
  PRIMARY KEY (`encoding_type`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`event`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`event` (
  `sid` INT(10) UNSIGNED NOT NULL ,
  `cid` INT(10) UNSIGNED NOT NULL ,
  `signature` INT(10) UNSIGNED NOT NULL ,
  `timestamp` DATETIME NOT NULL ,
  PRIMARY KEY (`sid`, `cid`) ,
  INDEX `sig` (`signature` ASC) ,
  INDEX `time` (`timestamp` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`icmphdr`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`icmphdr` (
  `sid` INT(10) UNSIGNED NOT NULL ,
  `cid` INT(10) UNSIGNED NOT NULL ,
  `icmp_type` TINYINT(3) UNSIGNED NOT NULL ,
  `icmp_code` TINYINT(3) UNSIGNED NOT NULL ,
  `icmp_csum` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `icmp_id` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `icmp_seq` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  PRIMARY KEY (`sid`, `cid`) ,
  INDEX `icmp_type` (`icmp_type` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`iphdr`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`iphdr` (
  `sid` INT(10) UNSIGNED NOT NULL ,
  `cid` INT(10) UNSIGNED NOT NULL ,
  `ip_src` INT(10) UNSIGNED NOT NULL ,
  `ip_dst` INT(10) UNSIGNED NOT NULL ,
  `ip_ver` TINYINT(3) UNSIGNED NULL DEFAULT NULL ,
  `ip_hlen` TINYINT(3) UNSIGNED NULL DEFAULT NULL ,
  `ip_tos` TINYINT(3) UNSIGNED NULL DEFAULT NULL ,
  `ip_len` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `ip_id` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `ip_flags` TINYINT(3) UNSIGNED NULL DEFAULT NULL ,
  `ip_off` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `ip_ttl` TINYINT(3) UNSIGNED NULL DEFAULT NULL ,
  `ip_proto` TINYINT(3) UNSIGNED NOT NULL ,
  `ip_csum` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  PRIMARY KEY (`sid`, `cid`) ,
  INDEX `ip_src` (`ip_src` ASC) ,
  INDEX `ip_dst` (`ip_dst` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`opt`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`opt` (
  `sid` INT(10) UNSIGNED NOT NULL ,
  `cid` INT(10) UNSIGNED NOT NULL ,
  `optid` INT(10) UNSIGNED NOT NULL ,
  `opt_proto` TINYINT(3) UNSIGNED NOT NULL ,
  `opt_code` TINYINT(3) UNSIGNED NOT NULL ,
  `opt_len` SMALLINT(6) NULL DEFAULT NULL ,
  `opt_data` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`sid`, `cid`, `optid`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`reference`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`reference` (
  `ref_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT ,
  `ref_system_id` INT(10) UNSIGNED NOT NULL ,
  `ref_tag` TEXT NOT NULL ,
  PRIMARY KEY (`ref_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`reference_system`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`reference_system` (
  `ref_system_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT ,
  `ref_system_name` VARCHAR(20) NULL DEFAULT NULL ,
  PRIMARY KEY (`ref_system_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`schema`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`schema` (
  `vseq` INT(10) UNSIGNED NOT NULL ,
  `ctime` DATETIME NOT NULL ,
  PRIMARY KEY (`vseq`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`sensor`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`sensor` (
  `sid` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT ,
  `hostname` TEXT NULL DEFAULT NULL ,
  `interface` TEXT NULL DEFAULT NULL ,
  `filter` TEXT NULL DEFAULT NULL ,
  `detail` TINYINT(4) NULL DEFAULT NULL ,
  `encoding` TINYINT(4) NULL DEFAULT NULL ,
  `last_cid` INT(10) UNSIGNED NOT NULL ,
  PRIMARY KEY (`sid`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`sig_class`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`sig_class` (
  `sig_class_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT ,
  `sig_class_name` VARCHAR(60) NOT NULL ,
  PRIMARY KEY (`sig_class_id`) ,
  INDEX `sig_class_id` (`sig_class_id` ASC) ,
  INDEX `sig_class_name` (`sig_class_name` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`sig_reference`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`sig_reference` (
  `sig_id` INT(10) UNSIGNED NOT NULL ,
  `ref_seq` INT(10) UNSIGNED NOT NULL ,
  `ref_id` INT(10) UNSIGNED NOT NULL ,
  PRIMARY KEY (`sig_id`, `ref_seq`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`signature`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`signature` (
  `sig_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT ,
  `sig_name` VARCHAR(255) NOT NULL ,
  `sig_class_id` INT(10) UNSIGNED NOT NULL ,
  `sig_priority` INT(10) UNSIGNED NULL DEFAULT NULL ,
  `sig_rev` INT(10) UNSIGNED NULL DEFAULT NULL ,
  `sig_sid` INT(10) UNSIGNED NULL DEFAULT NULL ,
  `sig_gid` INT(10) UNSIGNED NULL DEFAULT NULL ,
  PRIMARY KEY (`sig_id`) ,
  INDEX `sign_idx` (`sig_name`(20) ASC) ,
  INDEX `sig_class_id_idx` (`sig_class_id` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`tcphdr`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`tcphdr` (
  `sid` INT(10) UNSIGNED NOT NULL ,
  `cid` INT(10) UNSIGNED NOT NULL ,
  `tcp_sport` SMALLINT(5) UNSIGNED NOT NULL ,
  `tcp_dport` SMALLINT(5) UNSIGNED NOT NULL ,
  `tcp_seq` INT(10) UNSIGNED NULL DEFAULT NULL ,
  `tcp_ack` INT(10) UNSIGNED NULL DEFAULT NULL ,
  `tcp_off` TINYINT(3) UNSIGNED NULL DEFAULT NULL ,
  `tcp_res` TINYINT(3) UNSIGNED NULL DEFAULT NULL ,
  `tcp_flags` TINYINT(3) UNSIGNED NOT NULL ,
  `tcp_win` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `tcp_csum` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `tcp_urp` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  PRIMARY KEY (`sid`, `cid`) ,
  INDEX `tcp_sport` (`tcp_sport` ASC) ,
  INDEX `tcp_dport` (`tcp_dport` ASC) ,
  INDEX `tcp_flags` (`tcp_flags` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`udphdr`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`udphdr` (
  `sid` INT(10) UNSIGNED NOT NULL ,
  `cid` INT(10) UNSIGNED NOT NULL ,
  `udp_sport` SMALLINT(5) UNSIGNED NOT NULL ,
  `udp_dport` SMALLINT(5) UNSIGNED NOT NULL ,
  `udp_len` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  `udp_csum` SMALLINT(5) UNSIGNED NULL DEFAULT NULL ,
  PRIMARY KEY (`sid`, `cid`) ,
  INDEX `udp_sport` (`udp_sport` ASC) ,
  INDEX `udp_dport` (`udp_dport` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `barnyard`.`blacklist`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`blacklist` (
  `blacklist_id` INT NOT NULL AUTO_INCREMENT ,
  `ip` VARCHAR(45) NOT NULL ,
  `time_added` DATETIME NOT NULL ,
  `occurances` INT NULL ,
  `last_occurance` DATETIME NULL ,
  `severity` INT NULL ,
  PRIMARY KEY (`blacklist_id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `barnyard`.`bogon`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`bogon` (
  `bogon_id` INT NOT NULL AUTO_INCREMENT ,
  `ip-range` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`bogon_id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `barnyard`.`alert`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`alert` (
  `alert_id` INT NOT NULL AUTO_INCREMENT ,
  `alert_type` VARCHAR(45) NOT NULL ,
  `origin_ip` VARCHAR(45) NULL ,
  `destination_ip` VARCHAR(45) NULL ,
  `alert` TEXT NOT NULL ,
  `timestamp` DATETIME NULL ,
  PRIMARY KEY (`alert_id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `barnyard`.`domain_blacklist`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`domain_blacklist` (
  `dom_bl_id` INT NOT NULL ,
  `domain` VARCHAR(255) NULL ,
  `time_added` VARCHAR(255) NULL ,
  `domain_blacklistcol` VARCHAR(45) NULL ,
  PRIMARY KEY (`dom_bl_id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `barnyard`.`channel_blacklist`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `barnyard`.`channel_blacklist` (
  `channel_id` INT NOT NULL ,
  `channel_name` VARCHAR(45) NULL ,
  `time_added` VARCHAR(45) NULL ,
  `alert_alert_id` INT NOT NULL ,
  PRIMARY KEY (`channel_id`) ,
  INDEX `fk_channel_blacklist_alert_idx` (`alert_alert_id` ASC) ,
  CONSTRAINT `fk_channel_blacklist_alert`
    FOREIGN KEY (`alert_alert_id` )
    REFERENCES `barnyard`.`alert` (`alert_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
