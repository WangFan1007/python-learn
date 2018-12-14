

create table userinfo (
  id int primary key auto_increment,
  name varchar (15),
  email varchar (32)
) engine=InnoDB default charset=utf8;

create table hostinfo (
  id int primary key auto_increment,
  name char (64)
) engine=InnoDB default charset=utf8;


create table user_host_r (

  id int primary key auto_increment,
  u_id int,
  h_id int,
  unique (u_id,h_id),
  constraint foreign key (u_id) references userinfo(id),
  constraint foreign key (h_id) references hostinfo(id)
)engine=InnoDB default charset=utf8;