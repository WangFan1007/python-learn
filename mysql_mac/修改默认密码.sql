


set password for 'root'@'%' = password('root')

update user set password=password('root') where user='root' and host='localhost';

alter user user() identified by 'root';