-- Create a DATABASE with one Table
-- cat fortask2.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(id INTEGER UNIQUE, name VARCHAR(256));
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
INSERT INTO nexus6(id, name) VALUES(1, 'Leon');
SELECT * FROM nexus6;
