from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'Login'


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/logout')
def logout():
    return 'Logout'
