CREATE USER repl@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT REPLICATION SLAVE ON *.* TO repl@'%';

CHANGE MASTER TO MASTER_HOST='mysql-slave, MAS-TER_USER='replslave', MASTER_PASSWORD='password';

