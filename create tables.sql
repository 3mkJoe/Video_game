CREATE TABLE `game` ( 
  `game_id` INT AUTO_INCREMENT NOT NULL,
  `game_name` VARCHAR(250) NOT NULL,
  `score_id` INT NOT NULL,
  CONSTRAINT `PRIMARY` PRIMARY KEY (`game_id`)
);
CREATE TABLE `score` ( 
  `score_id` INT AUTO_INCREMENT NOT NULL,
  `score_number` INT NOT NULL,
  CONSTRAINT `PRIMARY` PRIMARY KEY (`score_id`)
);
CREATE TABLE `user` ( 
  `user_id` INT AUTO_INCREMENT NOT NULL,
  `username` VARCHAR(250) NOT NULL,
  `fullname` VARCHAR(250) NOT NULL,
  `password` VARCHAR(250) NOT NULL,
  `score_id` INT NOT NULL,
  CONSTRAINT `PRIMARY` PRIMARY KEY (`user_id`)
);
CREATE TABLE `user_game` ( 
  `user_game_id` INT AUTO_INCREMENT NOT NULL,
  `user_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  CONSTRAINT `PRIMARY` PRIMARY KEY (`user_game_id`)
);
SET FOREIGN_KEY_CHECKS = 0;
SET FOREIGN_KEY_CHECKS = 1;
ALTER TABLE `game` ADD CONSTRAINT `FK_game_score_id` FOREIGN KEY (`score_id`) REFERENCES `score` (`score_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `user` ADD CONSTRAINT `FK_user_score_id` FOREIGN KEY (`score_id`) REFERENCES `score` (`score_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `user_game` ADD CONSTRAINT `FK_user_game_game_id` FOREIGN KEY (`game_id`) REFERENCES `game` (`game_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `user_game` ADD CONSTRAINT `FK_user_game_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
