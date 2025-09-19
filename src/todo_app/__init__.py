from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Secret key for flash messages
    app.secret_key = "supersecretkey"

    # Database configuration (SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Import routes
    from .routes import register_routes
    register_routes(app)

    # Create database
    with app.app_context():
        db.create_all()

    return app
