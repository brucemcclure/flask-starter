from flask import Flask, jsonify                            # Import flask class and jsonify to send responses in JSON format
from marshmallow.exceptions import ValidationError          # Raises an error when validation fails on a field
from flask_sqlalchemy import  SQLAlchemy                    # This is the ORM
from flask_marshmallow import Marshmallow                   # Importing the Marshmallow class
from flask_bcrypt import Bcrypt                             # Hashing package
from flask_jwt_extended import JWTManager                   # Retrieves information form JWT
from flask_migrate import Migrate                           # Package to handle migrations

db = SQLAlchemy()                                           # New instance of SQLAlchemym named db
ma = Marshmallow()                                          # New instance of marshmallow named ma. This is for serialization
bcrypt = Bcrypt()                                           # New instance of Bcrypt, Hashing package
jwt = JWTManager()                                          # New instance of JWT Manager
migrate = Migrate()                                         # Makes new instance of migrate

def create_app():
    from dotenv import load_dotenv                          # Package to access environment variables
    load_dotenv()                                           # Retrieve the env variables from .env

    app = Flask(__name__)                                   # Creating an instnace of Flask named app
    app.config.from_object('default_settings.app_config')   # Loads the configuration for the app object from default_settings.py

    db.init_app(app)                                        # This is gives these packages context to the correct 'app' object
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db) 

    from commands import db_commands                        # Imports db_commands so they can be registered
    app.register_blueprint(db_commands)                     # Registering db_commands blueprint with app

    from controllers import registerable_controllers        # Import the registerable_controllers blueprint so it can be registered
    for controller in registerable_controllers:
        app.register_blueprint(controller)                  # Register each controller with app
    
    @app.errorhandler(ValidationError)                      # Inherits from Marshmallow ValidationError
    def handle_bad_request(error):  
        return(jsonify(error.messages), 400)                # Return a message with a 400

    @app.errorhandler(500)                                  # Handling the server error
    def handle_500(error):
        app.logger.error(error)
        return ("Server error: AKA bad stuff", 500)

    return app                                              # Return the app object