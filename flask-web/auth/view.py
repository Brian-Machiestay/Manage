#!/usr/bin/env python3
"""define an auth view for this application"""

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login')
def login():
    return 'Login'

@auth_blueprint.route('/signup')
def signup():
    return 'Signup'

@auth_blueprint.route('/logout')
def logout():
    return 'Logout'
