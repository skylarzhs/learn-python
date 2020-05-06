#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from sqlalchemy import Column, INTEGER, create_engine,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()

# 定义User对象


class User(Base):
    __tablename__ = 'test'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/his')
# 创建DBsession类型
DBSession = sessionmaker(bind=engine)

# 创建Session
session = DBSession()
# 创建Query查询
user = session.query(User).filter(User.id == 5).one()

print('type:',type(user))
print('name:',user.name)

session.close()
