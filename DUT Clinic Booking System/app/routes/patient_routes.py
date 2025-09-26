# app/routes/patient_routes.py
from flask import Blueprint, render_template

# This name must match the import in app/__init__.py
patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/')
def patient_home():
    return "Patient dashboard works!"
