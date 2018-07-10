#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask,request,render_template
from db_operation import item_operation
from typing import List

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

@app.route('/item_search',methods=['GET'])
def item_search_page():
    return render_template('item_search.html')

@app.route('/item_search',methods=['POST'])
def item_search():
    name = request.form['name']
    abbr = request.form['abbr']
    item_operation.item_search(name,abbr)
    return render_template('item_list.html',results=result)

if __name__ == '__main__':
    app.run()