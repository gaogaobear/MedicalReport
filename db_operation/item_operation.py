#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'用于数据库中检查项目名称，名称缩写，计量单位，上下限阈值的插入及修改'

import sqlite3
from time import *

#新增检查项目

def item_insert(name,abbr,unit,upper,lower):
    # 打开数据库
    conn = sqlite3.connect('MedicalReport.db')
    cursor = conn.cursor()
    sqlstr = 'INSERT INTO item (name,abbreviation,unit,UpperLimit,LowerLimit,create_time,update_time) \
     VALUES (\''+name+'\',\''+abbr+'\',\''+unit+'\',\''+upper+'\',\''+lower+'\',\''+strftime('%Y-%m-%d %H:%M:%S',localtime())+'\',\''+strftime('%Y-%m-%d %H:%M:%S',localtime())+'\')'
    cursor.execute(sqlstr)
    cursor.close()
    conn.commit()
    conn.close()


if __name__=='__main__':
    item_insert( name, abbr, unit, upper, lower)

