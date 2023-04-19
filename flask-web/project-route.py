#!/bin/env python3
"""define all routes for this project"""
from flask import Flask, abort
from flask import render_template
import models

app = Flask(__name__)


app.route('/', strict_slashes=False)
def root():
    """queries the root of this project"""
    return(render_template('index.html'))


app.route('/boards', strict_slashes=False)
def boards():
    """render the all boards page"""
    return(render_template('index.html'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

