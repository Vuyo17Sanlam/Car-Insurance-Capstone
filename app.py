from flask import Flask
from flask_login import LoginManager
from sqlalchemy.orm import Session

# from routes.car_insurance_bp import car_insurance_bp
from sqlalchemy.sql import text

from config import Config
from extensions import db
from models.user import User
from routes.admin_bp import admin_bp
from routes.car_insurance_bp import car_insurance_bp
from routes.user_bp import claims_page, user_bp

session = Session()


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)

    # Initialize the DB
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = (
        "user_bp.login_page"  # Redirects unauthorized users to the login page
    )

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)  # Maintain tokens for specific user

    with app.app_context():
        try:
            result = db.session.execute(text("SELECT * from users")).fetchall()
            print("Connection sucScessful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(car_insurance_bp)

    # app.register_blueprint(movies_bp, url_prefix="/movies")  # Refactor - Mailability ⬆️
    # app.register_blueprint(car_insurance_bp)  # Refactor - Mailability ⬆️
    # app.register_blueprint(user_bp, url_prefix="/movie-list")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
