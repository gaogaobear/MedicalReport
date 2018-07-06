from time import *


def test(a):
    sqlstr = 'insert into item(ab,cd) values ('+a+','+strftime('%Y-%m-%d %H:%M:%S',localtime())+')'
    return(sqlstr)

a= input('输入a\n')

print(test(a))