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



app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """queries the root of this project"""
    bd = Board.board('uuiddeessfff')
    print(bd.name)
    uid = uuid4()
    return(render_template('index.html', uid=uid))


@app.route('/boards', strict_slashes=False)
def boards():
    """render the all boards page"""
    return(render_template('index.html'))

@app.route('/createBoard', methods=['POST'], strict_slashes=False)
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


@app.route('/boards/<name>')
def getBoard(name):
    """render this board"""
    print(name)
    bd = Board.board_by_name(name.replace('_', ' '))
    print('this is the board')
    print(bd)
    print('done printing')
    if bd is None:
        res = make_response(jsonify({"error": "This board already exists"}))
        return res, 400
    other_bd = Board.get_other_boards(bd.name)
    return (render_template('board.html', bd=bd, other_bd=other_bd))

@app.route('/boards')
def allBoards():
    """render all boards"""
    return (render_template('all_boards.html'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

