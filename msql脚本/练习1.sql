--班级表
create table class (
  cid int primary key auto_increment,
  caption varchar (15)
);
--教师表
create table teacher (
  tid int primary key auto_increment,
  tname varchar(32)
);
--课程表
create table course (
  cid int primary key auto_increment,
  cname varchar (15),
  teacher_id int,
  constraint course_to_teacher foreign key (teacher_id) references teacher(tid)
);

--学生表
create table student(
  sid int primary key auto_increment,
  sname varchar(32),
  gender char,
  class_id int,
  constraint stu_class foreign key (class_id) references class(cid)
);

create table score(
  sid int primary key auto_increment,
  number int,
  student_id int,
  constraint foreign key (student_id) references student(sid),
  course_id int,
  constraint foreign key (course_id) references course(cid)
);

insert into class (cid, caption) values (1,'三年二班');
insert into class (cid, caption) values (2,'一年三班'),(3,'三年一班');


insert into teacher (tid, tname) values (1,'波多'),(2,'苍空'),(3,'饭岛');

insert into course (cid, cname, teacher_id) values
(1,'生物',1),
(2,'体育',1),
(3,'物理',2);

insert into student (sid, sname, gender, class_id) values
(1,'钢弹','女',1),
(2,'铁锤','女',1),
(3,'山炮','男',2);

insert into score (sid, number, student_id, course_id) values
(1,60,1,1),
(2,59,1,2),
(3,100,2,2);

--数据备份
mysqldump -uroot db1 > db1.sql -p
--数据库导入
mysqldump -uroot db1 < db1.sql -p

create table userinfo(
  id int auto_increment primary key,
  name char(15) not null ,
  password char (32) not null
);

insert into userinfo ( name, password) values ('wangfan','root');