#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: lqk  
@contact: 798244092@qq.com 
@site: https://github.com/lqkweb 
@file: manage.py 
@time: 2019/1/12 上午10:57 
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = "sqlsklearn基于python开发，支持通过写sql的方式实现各种机器学习算法"
    data = "欢迎使用开源项目：sqlsklearn"
    aim = "sqlsklearn：基于python开发，支持通过写sql的方式实现各种机器学习算法。"
    return render_template("index.html", title=title, data=data,aim=aim)

if __name__ == '__main__':
    app.run(port=5006)