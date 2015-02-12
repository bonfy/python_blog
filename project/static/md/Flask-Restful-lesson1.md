title: Flask-Restful-lesson1
date: 2014-09-11 21:18:44
---

仅以此文纪念我的Flask-Restful学习之路
先在开头介绍一下大神 [Miguelgrinberg](http://blog.miguelgrinberg.com/) 本文大部分借鉴了他的Restful文章

First Blood：

先上代码：
```python

# *-* coding:utf-8 *-*
from flask import render_template, flash, redirect, session, url_for, request, g
from flask import jsonify
from flask import abort
from flask import make_response
from app import app
from datetime import datetime

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

######################
#
# Personal function
#
######################

def getTaskByID(task_id,tasks):
	for task in tasks:
		print task
		if task['id'] == task_id:
			return task
	return None;


######################
#
# HTTP Status Handler
#
######################

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error':'Not Found 404' } ),404)
	
@app.errorhandler(400)
def error_400(error):
    return make_response(jsonify( { 'error':'Error 400' } ),400)

######################
#
# Route And RestFul
#
######################

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    return jsonify( { 'tasks': tasks } )

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'task': task } ), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = getTaskByID(task_id,tasks)
    if task == None:
        abort(404)
    return jsonify( { 'task': task } )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    task = getTaskByID(task_id, tasks)
    if task == None:
        abort(404)
    tasks.remove(task)
    return jsonify( { 'result': True } )

```

<!--more-->
这里看过大神文章的朋友都知道，这是他的不用　Flask-Restful API写的 Restful实现
这里主要就是将他的lamda 实现，用函数 get_task() 替代了 ，其他应该没什么差别
大家可以借鉴大神的blog，当然不用lamda只是本人的一种坚持，不知道在哪里看到的，flask对lamda支持不太行。。。。
