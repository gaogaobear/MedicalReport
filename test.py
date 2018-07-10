#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sqlite3
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/test',methods=['GET'])
def test_page():
    return render_template('test.html')

@app.route('/test',methods=['POST'])
def test():
    name = request.form['name']
    abbr = request.form['abbr']
    conn = sqlite3.connect('MedicalReport.db')
    cursor = conn.cursor()
    if len(name) == 0 and len(abbr) == 0:
        sqlstr = 'select id,name,abbreviation,unit,UpperLimit,LowerLimit,create_time,update_time from item order by id limit 1000'
    elif len(name) == 0 and len(abbr) > 0:
        sqlstr = 'select id,name,abbreviation,unit,UpperLimit,LowerLimit,create_time,update_time from item  where abbreviation like \'%' + abbr + '%\' order by id limit 1000'
    elif len(name) > 0 and len(abbr) == 0:
        sqlstr = 'select id,name,abbreviation,unit,UpperLimit,LowerLimit,create_time,update_time from item where name like \'%' + name + '%\' order by id limit 1000'
    elif len(name) > 0 and len(abbr) > 0:
        sqlstr = 'select id,name,abbreviation,unit,UpperLimit,LowerLimit,create_time,update_time from item where (name like \'%' + name + '%\' and abbreviation like \'%' + abbr + '%\' ) order by id limit 1000'
    cursor.execute(sqlstr)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return render_template('test_list.html',results=result)


if __name__ == '__main__':
    app.run()