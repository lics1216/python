# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。
# MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：

# 执行INSERT等操作后要调用commit()提交事务；
# MySQL的SQL占位符是%s。

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
# db = MySQLdb.connect(host="www.gyyx.com",user="user",passwd="xxx",db="mysql" )
# connect()的参数列表如下：
# host，连接的数据库服务器主机名，默认为本地主机(localhost)。
# user，连接数据库的用户名，默认为当前用户。
# passwd，连接密码，没有默认值。
# db，连接的数据库名，没有默认值。
conn = mysql.connector.connect(user='root', password='123456', database='lcs_test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()