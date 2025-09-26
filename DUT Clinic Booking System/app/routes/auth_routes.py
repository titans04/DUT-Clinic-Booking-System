from flask import Blueprint, render_template


# app/routes/auth_routes.py
from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return render_template('home.html')






auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return "Login page works!"
