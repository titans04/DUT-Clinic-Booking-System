from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TimeField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# ---------------- PATIENT FORMS ----------------
class PatientRegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(2, 50)])
    surname = StringField('Surname', validators=[DataRequired(), Length(2, 50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contact = StringField('Contact', validators=[DataRequired(), Length(10, 15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AppointmentForm(FlaskForm):
    service_type = SelectField('Service Type', choices=[('checkup', 'Check-Up'), ('vaccination', 'Vaccination'), ('followup', 'Follow-Up')], validators=[DataRequired()])
    preferred_date = DateField('Preferred Date', format='%Y-%m-%d', validators=[DataRequired()])
    preferred_time = TimeField('Preferred Time', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Book Appointment')

# ---------------- RECEPTIONIST FORMS ----------------
class ApproveAppointmentForm(FlaskForm):
    status = SelectField('Status', choices=[('Approved', 'Approved'), ('Rescheduled', 'Rescheduled'), ('Cancelled', 'Cancelled')], validators=[DataRequired()])
    doctor_id = SelectField('Assign Doctor', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Update Appointment')

# ---------------- NURSE FORMS ----------------
class NurseCheckInForm(FlaskForm):
    condition_status = SelectField('Condition Status', choices=[('Normal', 'Normal'), ('Stable', 'Stable'), ('Critical', 'Critical')], validators=[DataRequired()])
    vitals = TextAreaField('Vitals / Notes', validators=[DataRequired()])
    submit = SubmitField('Check-In')

# ---------------- DOCTOR FORMS ----------------
class MedicalRecordForm(FlaskForm):
    diagnosis = StringField('Diagnosis', validators=[DataRequired()])
    prescription = StringField('Prescription', validators=[DataRequired()])
    notes = TextAreaField('Consultation Notes', validators=[DataRequired()])
    condition_status = SelectField('Condition Status', choices=[('Normal', 'Normal'), ('Stable', 'Stable'), ('Critical', 'Critical')], validators=[DataRequired()])
    submit = SubmitField('Save Record')
