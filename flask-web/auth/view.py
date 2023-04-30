#!/usr/bin/env python3
"""define an auth view for this application"""

from flask import Blueprint, render_template


auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login')
def login():
    return(render_template('auth/login.html'))

@auth_blueprint.route('/signup')
def signup():
    return(render_template('auth/signup.html'))

@auth_blueprint.route('/logout')
def logout():
    return 'Logout'
