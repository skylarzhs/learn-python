#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='his')

cursor = conn.cursor()

# cursor.execute('create table test(id int primary key auto_increment,name varchar(20))engine=innodb')

cursor.execute('insert into test value(5,"Skylar")')

count = cursor.rowcount

conn.commit()

cursor.close()

cursor = conn.cursor()

cursor.execute('select * from test where id > %s', (1,))

values = cursor.fetchall()

print(values)

cursor.close()

conn.close()
