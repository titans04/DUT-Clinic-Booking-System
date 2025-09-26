from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.routes.auth_routes import auth_bp
    from app.routes.patient_routes import patient_bp
    from app.routes.receptionist_routes import receptionist_bp
    from app.routes.doctor_routes import doctor_bp
    from app.routes.nurse_routes import nurse_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(patient_bp, url_prefix='/patient')
    app.register_blueprint(receptionist_bp, url_prefix='/receptionist')
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
    app.register_blueprint(nurse_bp, url_prefix='/nurse')

    return app
