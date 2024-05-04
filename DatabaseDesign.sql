-- Web-Application Part
CREATE TABLE `defaultdb`.`applicant_information` (
  `application_id` VARCHAR(7) NOT NULL,
  `fullname` VARCHAR(60) NULL,
  `citizen_id` VARCHAR(13) NULL,
  `contact_number` VARCHAR(12) NULL,
  `email` VARCHAR(40) NULL,
  `age` INT NULL,
  `DOB` VARCHAR(10) NULL,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(60) NULL,
  `nationality` VARCHAR(15) NULL,
  `religion` VARCHAR(20) NULL,
  `university` VARCHAR(50) NULL,
  `degree` VARCHAR(45) NULL,
  `GPA` VARCHAR(5) NULL,
  `address` VARCHAR(150) NULL,
  `gender` VARCHAR(10) NULL,
  `martial_status` INT NULL,
  `military_status` INT NULL,
  `workingexp_id` VARCHAR(7) NULL,
  `emergencycont_id` VARCHAR(7) NULL,
  `partnerinfo_id` VARCHAR(7) NULL,
  `append_date` DATETIME NULL,
  PRIMARY KEY (`application_id`),
  UNIQUE INDEX `application_id_UNIQUE` (`application_id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`partner_information` (
  `partnerinfo_id` VARCHAR(7) NOT NULL,
  `fullname` VARCHAR(60) NULL,
  `occupation` VARCHAR(100) NULL,
  `company` VARCHAR(100) NULL,
  `number_of_spouse` INT NULL,
  `contact_number` VARCHAR(12) NULL,
  `email` VARCHAR(40) NULL,
  `address` VARCHAR(150) NULL,
  PRIMARY KEY (`pi_id`));
  UNIQUE INDEX `pi_id_UNIQUE` (`pi_id` ASC) VISIBLE;

CREATE TABLE `defaultdb`.`emergency_contact` (
  `emergencycont_id` VARCHAR(7) NOT NULL,
  `fullname` VARCHAR(60) NULL,
  `contact_number` VARCHAR(12) NULL,
  `relationship` VARCHAR(20) NULL,
  `additional_fullname` VARCHAR(60) NULL,
  `additional_contact_number` VARCHAR(30) NULL,
  `additional_relationship` VARCHAR(40) NULL,
  PRIMARY KEY (`emergencycont_id`),
  UNIQUE INDEX `emergencycont_id_UNIQUE` (`emergencycont_id` ASC) VISIBLE);


CREATE TABLE `defaultdb`.`working_experiences` (
  `workingexp_id` VARCHAR(7) NOT NULL,
  `document_path` VARCHAR(100) NULL,
  `statement_of_purpose` VARCHAR(2500) NULL,
  `driving_license` INT NULL,
  `car_possession` INT NULL,
  `pc_possession` INT NULL,
  `foreign_language` VARCHAR(150) NULL,
  `proficiency` VARCHAR(250) NULL,
  `special_ability` VARCHAR(250) NULL,
  PRIMARY KEY (`workingexp_id`),
  UNIQUE INDEX `workingexp_id_UNIQUE` (`workingexp_id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`organization_information` (
  `position_id` INT NOT NULL AUTO_INCREMENT,
  `department` VARCHAR(45) NULL,
  `position` VARCHAR(45) NULL,
  `competencies` VARCHAR(500) NULL,
  `skills` text(1500) NULL,
  `skills_map` text(1500) NULL,
  PRIMARY KEY (`position_id`),
  UNIQUE INDEX `position_id_UNIQUE` (`position_id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`employee_information` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `fullname` VARCHAR(60) NULL,
  `position_id` INT NULL,
  `role` VARCHAR(45) NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE INDEX `employee_id_UNIQUE` (`employee_id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`job_information` (
  `job_id` INT NOT NULL AUTO_INCREMENT,
  `position_id` INT NULL,
  `position` VARCHAR(45) NULL,
  `department` VARCHAR(45) NULL,
  `approx_salary` VARCHAR(45) NULL,
  `number_of_applicants` INT NULL,
  `start_date` VARCHAR(10) NULL,
  `application_deadline` VARCHAR(10) NULL,
  `line_manager_id` INT NULL,
  `working_location` VARCHAR(100) NULL,
  `educational_degree_required` VARCHAR(250) NULL,
  `required_experiences` VARCHAR(250) NULL,
  `required_skills` VARCHAR(250) NULL,
  `status` VARCHAR(45) NULL,
  `working_time_details` VARCHAR(45) NULL,
  `job_description` VARCHAR(1500) NULL,
  `accommodations` VARCHAR(250) NULL,
  `bonus` VARCHAR(45) NULL,
  `transportation` VARCHAR(45) NULL,
  `transportation_allowances` VARCHAR(45) NULL,
  `ot_per_hour` INT NULL,
  `leave_quota` VARCHAR(45) NULL,
  `laptop_provision` VARCHAR(45) NULL,
  `other_provision` VARCHAR(45) NULL,
  `insurance_provision` VARCHAR(45) NULL,
  `insurance_level` INT NULL,
  `additional_benefits_welfare` VARCHAR(1000) NULL,
  PRIMARY KEY (`job_id`),
  UNIQUE INDEX `job_id_UNIQUE` (`job_id` ASC) VISIBLE);

ALTER TABLE `defaultdb`.`applicant_information` 
ADD INDEX `emergencycont_id_idx` (`emergencycont_id` ASC) VISIBLE,
ADD INDEX `partnerinfo_id_idx` (`partnerinfo_id` ASC) VISIBLE,
ADD INDEX `workingexp_id_idx` (`workingexp_id` ASC) VISIBLE;
;
ALTER TABLE `defaultdb`.`applicant_information` 
ADD CONSTRAINT `emergencycont_id`
  FOREIGN KEY (`emergencycont_id`)
  REFERENCES `defaultdb`.`emergency_contact` (`emergencycont_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `partnerinfo_id`
  FOREIGN KEY (`partnerinfo_id`)
  REFERENCES `defaultdb`.`partner_information` (`partnerinfo_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `workingexp_id`
  FOREIGN KEY (`workingexp_id`)
  REFERENCES `defaultdb`.`working_experiences` (`workingexp_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `defaultdb`.`job_information` 
ADD CONSTRAINT `position_id`
  FOREIGN KEY (`position_id`)
  REFERENCES `defaultdb`.`organization_information` (`position_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `employee_id`
  FOREIGN KEY (`line_manager_id`)
  REFERENCES `defaultdb`.`employee_information` (`employee_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

CREATE TABLE `defaultdb`.`questions` (
  `question_id` INT NOT NULL AUTO_INCREMENT,
  `question` VARCHAR(150) NULL,
  `question_type` VARCHAR(45) NULL,
  `question_category` VARCHAR(45) NULL,
  `question_difficulty` VARCHAR(10) NULL,
  `question_position` VARCHAR(250) NULL,
  `question_keywords` VARCHAR(1000) NULL,
  PRIMARY KEY (`question_id`),
  UNIQUE INDEX `question_id_UNIQUE` (`question_id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`application` (
  `application_id` INT NOT NULL AUTO_INCREMENT,
  `applicant_id` VARCHAR(7) NULL,
  `job_id` INT NULL,
  `registered_datetime` DATETIME NULL,
  PRIMARY KEY (`application_id`),
  UNIQUE INDEX `application_id_UNIQUE` (`application_id` ASC) VISIBLE);

ALTER TABLE `defaultdb`.`application` 
ADD INDEX `applicant_id_idx` (`applicant_id` ASC) VISIBLE,
ADD INDEX `job_id_idx` (`job_id` ASC) VISIBLE;
;
ALTER TABLE `defaultdb`.`application` 
ADD CONSTRAINT `applicant_id`
  FOREIGN KEY (`applicant_id`)
  REFERENCES `defaultdb`.`applicant_information` (`application_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `job_id`
  FOREIGN KEY (`job_id`)
  REFERENCES `defaultdb`.`job_information` (`job_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

CREATE TABLE `defaultdb`.`questions_answered` (
  `qa_id` INT NOT NULL AUTO_INCREMENT,
  `application_id` INT NULL,
  `question_id` INT NULL,
  `answer` VARCHAR(5000) NULL,
  PRIMARY KEY (`qa_id`),
  UNIQUE INDEX `qa_id_UNIQUE` (`qa_id` ASC) VISIBLE);

ALTER TABLE `defaultdb`.`questions_answered` 
ADD INDEX `application_id_idx` (`application_id` ASC) VISIBLE,
ADD INDEX `question_id_idx` (`question_id` ASC) VISIBLE;
;
ALTER TABLE `defaultdb`.`questions_answered` 
ADD CONSTRAINT `application_id`
  FOREIGN KEY (`application_id`)
  REFERENCES `defaultdb`.`application` (`application_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `question_id`
  FOREIGN KEY (`question_id`)
  REFERENCES `defaultdb`.`questions` (`question_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

CREATE TABLE `defaultdb`.`job_questions` (
  `jq_id` INT NOT NULL AUTO_INCREMENT,
  `job_id` INT NULL,
  `question_id` INT NULL,
  PRIMARY KEY (`jq_id`),
  UNIQUE INDEX `jobques_id_UNIQUE` (`jq_id` ASC) VISIBLE);

ALTER TABLE `defaultdb`.`job_questions` 
ADD INDEX `jb_id_idx` (`job_id` ASC) VISIBLE,
ADD INDEX `ques_id_idx` (`question_id` ASC) VISIBLE;
;
ALTER TABLE `defaultdb`.`job_questions` 
ADD CONSTRAINT `jb_id`
  FOREIGN KEY (`job_id`)
  REFERENCES `defaultdb`.`job_information` (`job_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `ques_id`
  FOREIGN KEY (`question_id`)
  REFERENCES `defaultdb`.`questions` (`question_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


-- Data Analysis Part
CREATE TABLE `defaultdb`.`analysis_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `applicant_id` VARCHAR(7) NULL,
  `fullname` VARCHAR(60) NULL,
  `position` VARCHAR(45) NULL,
  `degree` VARCHAR(45) NULL,
  `text_extracted` TEXT(10000) NULL,
  `skills_list` TEXT(10000) NULL,
  `statement_of_purpose` VARCHAR(2500) NULL,
  `init_question_list` TEXT(10000) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`result_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `applicant_id` VARCHAR(45) NULL,
  `final_questions_id_list` VARCHAR(1000) NULL,
  `final_questions_list` TEXT(10000) NULL,
  `resume_score` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`EMSI_api_skills` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `skills_id` VARCHAR(45) NULL,
  `infoUrl` VARCHAR(200) NULL,
  `skill_name` VARCHAR(100) NULL,
  `skill_type_id` VARCHAR(20) NULL,
  `skill_type` VARCHAR(50) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
