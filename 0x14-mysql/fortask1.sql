-- creates the MySQL server user user_0d_1
-- with REPLICATION CLIENT privileges.
-- Enables use of the SHOW MASTER STATUS, SHOW SLAVE STATUS, and SHOW BINARY LOGS statements.
-- Grant this privilege to accounts that are used by slave servers to connect to the
-- current server as their master.
-- cat fortask1.sql | mysql -hlocalhost -uroot -p
-- for see the changes:
-- mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"

CREATE USER IF NOT EXISTS holberton_user@localhost
IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO holberton_user@localhost;
