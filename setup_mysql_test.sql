-- create a new database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

USE hbnb_test_db;

-- giving all privileges on the database `hbnb_test_db`
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- SELECT privilege on the database `performance_schema`
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
