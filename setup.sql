-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS manage;
CREATE USER IF NOT EXISTS 'brian'@'localhost' IDENTIFIED BY 'developer';
GRANT ALL PRIVILEGES ON `manage`.* TO 'brian'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'brian'@'localhost';
FLUSH PRIVILEGES;
