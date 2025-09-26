from flask import Blueprint

# The name must match exactly what is imported in app/__init__.py
receptionist_bp = Blueprint('receptionist', __name__)

@receptionist_bp.route('/')
def receptionist_home():
    return "Receptionist dashboard works!"
