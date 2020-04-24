-- config user for replica server
-- cat fortask3.sql | mysql -hlocalhost -uroot -p
CREATE USER IF NOT EXISTS 'replica_user'@'%'
IDENTIFIED BY 'rep_pwd';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

