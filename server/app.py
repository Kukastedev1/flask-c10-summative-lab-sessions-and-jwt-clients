from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt, migrate
from routes.auth_routes import auth_bp
from routes.resource_routes import resource_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #  Enable CORS (important for React frontend)
    CORS(app, supports_credentials=True)

    #  Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    #  Register blueprints
    # If your frontend uses plain routes like /login, /notes → keep this:
    app.register_blueprint(auth_bp)
    app.register_blueprint(resource_bp)

  

    # Simple health check route (useful for testing)
    @app.route("/")
    def home():
        return {"message": "API is running"}, 200

    return app


# Create app instance
app = create_app()


if __name__ == "__main__":
    app.run(debug=True)