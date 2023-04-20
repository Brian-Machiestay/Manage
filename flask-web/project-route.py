#!/bin/env python3
"""define all routes for this project"""
from flask import Flask, abort
from flask import render_template
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
    print(bd)
    uid = uuid4()
    return(render_template('index.html', uid=uid))


@app.route('/boards', strict_slashes=False)
def boards():
    """render the all boards page"""
    return(render_template('index.html'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

