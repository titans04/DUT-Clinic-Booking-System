from . import db
from flask_login import UserMixin

# ---------------- PATIENT ----------------
class Patient(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    appointments = db.relationship('Appointment', backref='patient', lazy=True)

# ---------------- DOCTOR ----------------
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String(200), nullable=False)  # e.g., "Mon-Fri 08:00-16:00"

    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

# ---------------- RECEPTIONIST ----------------
class Receptionist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)

    appointments = db.relationship('Appointment', backref='receptionist', lazy=True)

# ---------------- NURSE ----------------
class Nurse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    availability = db.Column(db.String(200), nullable=False)

    appointments = db.relationship('Appointment', backref='nurse', lazy=True)

# ---------------- APPOINTMENT ----------------
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    receptionist_id = db.Column(db.Integer, db.ForeignKey('receptionist.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    nurse_id = db.Column(db.Integer, db.ForeignKey('nurse.id'), nullable=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pending")  # Pending, Approved, Completed, Cancelled

    medical_record = db.relationship('MedicalRecord', backref='appointment', uselist=False)

# ---------------- MEDICAL RECORD ----------------
class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    diagnosis = db.Column(db.String(200), nullable=True)
    prescription = db.Column(db.String(200), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    condition_status = db.Column(db.String(50), nullable=True)  # Normal, Stable, Critical
