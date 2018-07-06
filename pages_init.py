#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask,request,render_template
from db_operation import item_operation

app = Flask(__name__)

@app.route('/item_insert',methods=['GET'])
def item_insert_page():
    return render_template('item_insert.html')

@app.route('/item_insert',methods=['POST'])
def it_insert():
    name = request.form['name']
    abbr = request.form['abbr']
    unit = request.form['unit']
    upper = request.form['upper']
    lower = request.form['lower']
    item_operation.item_insert(name,abbr,unit,upper,lower)
    return render_template('insert_ok.html')

if __name__ == '__main__':
    app.run()