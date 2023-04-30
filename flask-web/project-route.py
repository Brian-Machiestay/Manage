#!/bin/env python3
"""define all routes for this project"""
from flask import Flask, abort, request, jsonify
from flask import render_template, make_response
from uuid import uuid4
import models
from flask_cors import CORS
from models.board import Board
from models.items import Item
from models.subtasks import Subtask
from models.task import Task
from api.v1.views import app_views
import json
from auth.view import auth_blueprint


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.register_blueprint(auth_blueprint)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/', strict_slashes=False)
def root():
    """queries the root of this project"""
    uid = uuid4()
    count = Board.count_boards()
    boards = Board.boards()
    return(render_template('allboard.html', uid=uid, count=count, boards=boards))


@app.route('/boards', strict_slashes=False)
def boards():
    """render the all boards page"""
    count = Board.count_boards()
    boards = Board.boards()
    return(render_template('allboard.html', count=count, boards=boards))



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
    uid = uuid4()
    count = Board.count_boards()
    return (render_template('board.html', bd=bd, other_bd=other_bd, uid=uid, count=count))

@app.route('/boards')
def allBoards():
    """render all boards"""
    boards = Board.boards()
    count = Board.count_boards()
    return (render_template('allboards.html', count=count, boards=boards))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
