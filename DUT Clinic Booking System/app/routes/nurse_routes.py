# app/routes/nurse_routes.py
from flask import Blueprint, render_template

# Must match the import in app/__init__.py
nurse_bp = Blueprint('nurse', __name__)

@nurse_bp.route('/')
def nurse_home():
    return "Nurse dashboard works!"

