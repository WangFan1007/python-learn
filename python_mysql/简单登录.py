import pymysql

'''
create table userinfo(
  id int auto_increment primary key,
  name char(15) not null ,
  password char (32) not null
);

insert into userinfo ( name, password) values ('wangfan','root');
'''


user = input("username:")
pwd = input("password:")
conn = pymysql.connect(host="localhost",user="root",password='root',database='db1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# swafd' or 1=1 --
# sql = "select * from userinfo where name='%s' and password='%s'"%(user,pwd,)

sql = "select * from userinfo where name=%s and password=%s"
print(sql)
cursor.execute(sql,(user,pwd))
result = cursor.fetchone()
cursor.close()
conn.close()
print(result)