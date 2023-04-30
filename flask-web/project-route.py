#!/bin/env python3
"""define all routes for this project"""
from flask import Flask, abort, request, jsonify
from flask import render_template, make_response
from uuid import uuid4
import models
from flask_cors import CORS
from models.board import Board
from models.items import Item
from models.user import User
from models.subtasks import Subtask
from models.task import Task
from api.v1.views import app_views
import json
from auth.view import auth_blueprint
from flask_login import LoginManager, login_required, current_user


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = 'brian'
app.register_blueprint(app_views)
app.register_blueprint(auth_blueprint)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """tell login manager how to load a user"""
    return models.storage.user_by_id(user_id)

@app.route('/', strict_slashes=False)
@login_required
def root():
    """queries the root of this project"""
    print(current_user.is_authenticated)
    uid = uuid4()
    usr = current_user
    count = Board.count_boards(usr.id)
    boards = Board.boards(usr.id)
    return(render_template('allboard.html', uid=uid, count=count, boards=boards))


@app.route('/boards', strict_slashes=False)
@login_required
def boards():
    """render the all boards page"""
    usr = current_user
    uid = uuid4()
    count = Board.count_boards(usr.id)
    boards = Board.boards(usr.id)
    return(render_template('allboard.html', count=count, boards=boards, uid=uid))



@app.route('/boards/<name>')
@login_required
def getBoard(name):
    """render this board"""
    print(name)
    usr = current_user
    bd = Board.board_by_name(usr.id, name.replace('_', ' '))
    if bd is None:
        res = make_response(jsonify({"error": "This board already exists"}))
        return res, 400
    other_bd = Board.get_other_boards(usr.id, bd.name)
    uid = uuid4()
    count = Board.count_boards(usr.id)
    return (render_template('board.html', bd=bd, other_bd=other_bd, uid=uid, count=count))

@app.route('/boards')
def allBoards():
    """render all boards"""
    boards = Board.boards()
    count = Board.count_boards()
    return (render_template('allboards.html', count=count, boards=boards))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
