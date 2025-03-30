from flask import Flask
from sqlalchemy.sql import text

from config import Config
from extensions import db
from models.user import User
from routes.user_bp import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the D
    db.init_app(app)

    with app.app_context():
        try:
            result = db.session.execute(text("SELECT * from clients")).fetchall()
            print("Connection successful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    app.register_blueprint(user_bp)
    # app.register_blueprint(movies_bp, url_prefix="/movies")  # Refactor - Mailability ⬆️
    # app.register_blueprint(movies_list_bp, url_prefix="/movie-list")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
