#!/usr/bin/env python3
"""define an auth view for this application"""

from flask import Blueprint, render_template, url_for, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
import models


auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login')
def login():
    """render the login page"""
    return(render_template('auth/login.html'))

@auth_blueprint.route('/login', methods=['POST'])
def login_post():
    """handle post request for login"""
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    usr = models.storage.user_by_email(email)
    if not usr or not check_password_hash(usr.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    return redirect(url_for('root'))

@auth_blueprint.route('/signup')
def signup():
    """render the signup page"""
    return(render_template('auth/signup.html'))

@auth_blueprint.route('/signup', methods=['POST'])
def signup_post():
    """handle the signup"""
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    usr = models.storage.user_by_email(email)
    if usr:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    user_new = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))
    user_new.save()
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/logout')
def logout():
    return 'Logout'
