
#主键可以有多列主键组成
create table t1 (
  nid int(11) not null auto_increment,
  pid int(11) not null,
  num int(11) default null,
  primary key (nid,pid)

) engine=InnoDB default charset=utf8;

#外键可以有多个
create table t2 (
  id int auto_increment primary key,
  name char(10),
  id1 int,
  id2 int,
  constraint foreign key (id1,id2) references t1(nid, pid)
) engine=InnoDB default charset=utf8;


delete from t1; #自增id
truncate table t1; #自增ID设置为1

insert into t1(pid,num) values (1,11),(2,33),(3,44);

desc t1;

show create table t1 \G;

alter table t1 AUTO_INCREMENT=2;