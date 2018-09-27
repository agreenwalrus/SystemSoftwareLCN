-- DROP DATABASE IF EXISTS trtpo_system;
SET NAMES 'utf8';
SET SESSION collation_connection = 'utf8_general_ci';

CREATE DATABASE trtpo_system DEFAULT CHARACTER SET 'utf8';

USE trtpo_system;

CREATE TABLE users(
id_user INTEGER AUTO_INCREMENT,
username VARCHAR(100),
password VARCHAR(100),
id_lecturer INTEGER,
PRIMARY KEY(id_user)
);

CREATE TABLE lecturers(
id_lecturer INTEGER AUTO_INCREMENT,
full_name VARCHAR(100) NOT NULL,
PRIMARY KEY(id_lecturer)
);

CREATE TABLE  groups(
id_group INTEGER AUTO_INCREMENT,
group_number VARCHAR(20),
bsuir_api_group_id VARCHAR(20) NOT NULL,
amount_of_test INTEGER NOT NULL,
PRIMARY KEY(id_group)
);

CREATE TABLE groups_subgroups (
id_group_subgroup INTEGER AUTO_INCREMENT,
id_group INTEGER,
id_lecturer INTEGER,
PRIMARY KEY(id_group_subgroup)
);

CREATE TABLE subgroups (
id_subgroup int AUTO_INCREMENT,
id_group_subgroup INTEGER,
subgroup_number varchar(5) NOT NULL,
PRIMARY KEY(id_subgroup),
FOREIGN KEY(id_group_subgroup) REFERENCES groups_subgroups(id_group_subgroup)
);

CREATE TABLE students(
id_student int AUTO_INCREMENT,
full_name varchar(100) NOT NULL,
git_user_name varchar(30) NOT NULL,
git_repo_name varchar(30) NOT NULL,
email varchar(30) NULL,
id_group_subgroup int,
PRIMARY KEY(id_student),
FOREIGN KEY(id_group_subgroup) REFERENCES groups_subgroups(id_group_subgroup)
);

CREATE TABLE absentees(
id_absence INTEGER AUTO_INCREMENT,
id_class INTEGER,
id_student INTEGER,
PRIMARY KEY(id_absence)
);

CREATE TABLE classes(
id_class INTEGER AUTO_INCREMENT,
class_date DATETIME NOT NULL,
id_group_subgroup INTEGER,
PRIMARY KEY(id_class)
);

CREATE TABLE issued_labs(
id_issued_lab INTEGER AUTO_INCREMENT,
id_lab INTEGER ,
id_group_subgroup INTEGER,
id_class_of_issue INTEGER,
coefficient DOUBLE NOT NULL,
id_class_deadline INTEGER,
last_check_date_time DATETIME NOT NULL,
PRIMARY KEY(id_issued_lab)
);

CREATE TABLE labs(
id_lab INTEGER AUTO_INCREMENT,
lab_number INTEGER NOT NULL,
key_word VARCHAR(20) NOT NULL,
PRIMARY KEY(id_lab)
);

CREATE TABLE labs_marks(
id_lab_mark INTEGER AUTO_INCREMENT,
id_student INTEGER,
id_issued_lab INTEGER,
coefficient DOUBLE NOT NULL,
mark INTEGER NOT NULL,
PRIMARY KEY(id_lab_mark)
);

CREATE TABLE tests(
id_test INTEGER AUTO_INCREMENT,
test_number INTEGER NOT NULL,
test_date TIMESTAMP NOT NULL,
PRIMARY KEY(id_test)
);

CREATE TABLE tests_result(
id_test_result INTEGER AUTO_INCREMENT,
id_student INTEGER,
id_test INTEGER,
mark INTEGER NOT NULL,
PRIMARY KEY(id_test_result),
FOREIGN KEY(id_test) REFERENCES tests(id_test)
);

CREATE TABLE bonuses(
id_bonus INTEGER AUTO_INCREMENT,
id_student INTEGER,
bonus INTEGER NOT NULL,
PRIMARY KEY(id_bonus)
);
