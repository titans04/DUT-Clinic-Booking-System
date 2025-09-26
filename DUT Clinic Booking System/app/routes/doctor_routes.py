# app/routes/doctor_routes.py
from flask import Blueprint, render_template

# Must match the import in app/__init__.py
doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/')
def doctor_home():
    return "Doctor dashboard works!"
