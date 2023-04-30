#!/bin/env python3
"""define all routes for this project"""
from flask import Flask, abort, request, jsonify
from flask import render_template, make_response
from uuid import uuid4
import models
from models.board import Board
from models.items import Item
from models.subtasks import Subtask
from models.task import Task
import json
from api.v1.views import app_views



@app_views.route('/createBoard', methods=['POST'], strict_slashes=False)
def createBoard():
    """create a new board"""
    bd_name = request.form.get('name', None)
    if bd_name is None:
        res = make_response(jsonify({"error": "board name cannot be null"}))
        return res, 400
    elif bd_name.strip() == '':
        res = make_response(jsonify({"error": "board name cannot be null"}))
        return res, 400

    bd = Board(bd_name.strip())
    try:
        bd.save()
        print(bd)
        return(jsonify({
            'name': bd.name.replace(' ', '_')
        }))
    except(Exception):
        res = make_response(jsonify({"error": "This board already exists"}))
        return res, 400


@app_views.route('/createColumn', methods=['POST'], strict_slashes=False)
def createColumn():
    """create a new column"""
    colname = request.form.get('name', None)
    boardname = request.form.get('board', None)
    if colname is None:
        res = make_response(jsonify({"error": "Column name cannot be null"}))
        return res, 400
    elif colname.strip() == '':
        res = make_response(jsonify({"error": "Column name cannot be null"}))
        return res, 400

    bd = Board.board_by_name(boardname.strip())
    print('board: {}'.format(bd))
    col = Item(colname.strip(), bd.id)
    print('item: {}'.format(col))
    try:
        col.save()
        print(col)
        return(jsonify({
            'name': col.name,
            'id': col.id
        }))
    except(Exception):
        res = make_response(jsonify({"error": "This column already exists"}))
        return res, 400

@app_views.route('/createTask', methods=['POST'], strict_slashes=False)
def createTask():
    """create a task"""
    print(request.form)
    bdName = request.form.get('boardName', None)
    itName = request.form.get('item', None)
    if itName == '' or itName is None:
        res = make_response(jsonify({"error": "create an item"}))
        return res, 400
    subtasks = request.form.get('subtasks', None)
    item = Item.get_item_by_name(itName, bdName)
    des = request.form.get('des', None)
    if des is None or des.strip() == '':
        print('bad description')
        res = make_response(jsonify({"error": "Description must be provided"}))
        return res, 400
    title = request.form.get('task_title', None)
    if title is None or title.strip() == '':
        print('bad title')
        res = make_response(jsonify({"error": "title must be provided"}))
        return res, 400
    task = Task(title, des, item.id)
    task.save()
    for sub in json.loads(subtasks):
        sb = Subtask(sub, task.id)
        sb.save()
    tk = Task.get_task(task.id)
    it_d = dict()
    task_dict = dict()
    task_dict['title'] = tk.title
    task_dict['des'] = tk.description
    task_dict['subtasks'] = dict()
    for sub in tk.subtasks:
        sub_dict = dict()
        sub_dict['title'] = sub.title
        sub_dict['status'] = sub.status
        task_dict['subtasks'][sub.id] = sub_dict
    it_d['item_id'] = item.id
    it_d['task'] = task_dict
    it_d['task_id'] = tk.id
    it_d['name'] = item.name
    print(it_d)
    return(it_d)



@app_views.route('/board_data', methods=['POST'], strict_slashes=False)
def get_board_data():
    """return all data assiocated with this board"""
    bdName = request.form.get('board', None)
    print('board name: {}'.format(bdName))
    bd = Board.board_by_name(bdName)
    print(bd.items)
    ob = dict()
    for it in bd.items:
        ob[it.id] = dict()
        tasks = dict()
        for tk in it.tasks:
            task_dict = dict()
            task_dict['title'] = tk.title
            task_dict['des'] = tk.description
            task_dict['subtasks'] = dict()
            for sub in tk.subtasks:
                sub_dict = dict()
                sub_dict['title'] = sub.title
                sub_dict['status'] = sub.status
                task_dict['subtasks'][sub.id] = sub_dict
            tasks[tk.id] = task_dict
        ob[it.id]['name'] = it.name
        ob[it.id]['tasks'] = tasks
    print(ob)
    return(ob)
