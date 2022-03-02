CREATE TABLE `accounting_account` (
	`code_a` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	PRIMARY KEY (`code_a`) USING BTREE
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;

CREATE TABLE `cost_center` (
	`code_c` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	PRIMARY KEY (`code_c`) USING BTREE
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;

CREATE TABLE `enterprise` (
	`code_e` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	PRIMARY KEY (`code_e`) USING BTREE
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;

CREATE TABLE `unit` (
	`code_u1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	PRIMARY KEY (`code_u1`) USING BTREE
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;

CREATE TABLE `management` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`enum` ENUM('expense','admission') NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`date` DATE NOT NULL,
	`n_reference` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`n_bill` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`n_receipt` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`code_e1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`code_c1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`code_a1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`concept` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`quantity` FLOAT NOT NULL,
	`code_u1` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`price` FLOAT NOT NULL,
	PRIMARY KEY (`id`) USING BTREE,
	INDEX `code_e1` (`code_e1`) USING BTREE,
	INDEX `code_c1` (`code_c1`) USING BTREE,
	INDEX `code_a1` (`code_a1`) USING BTREE,
	INDEX `code_u1` (`code_u1`) USING BTREE,
	CONSTRAINT `FK_management_unit` FOREIGN KEY (`code_u1`) REFERENCES `economic_management`.`unit` (`code_u1`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `FK__accounting_account` FOREIGN KEY (`code_a1`) REFERENCES `economic_management`.`accounting_account` (`code_a`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `FK__cost_center` FOREIGN KEY (`code_c1`) REFERENCES `economic_management`.`cost_center` (`code_c`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `FK__enterprise` FOREIGN KEY (`code_e1`) REFERENCES `economic_management`.`enterprise` (`code_e`) ON UPDATE NO ACTION ON DELETE NO ACTION
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;
