from models.User import User                                                 # Importing the User Model
from schemas.UserSchema import user_schema                                   # Importing the User Schema
from main import db                                                          # This is the db instance created by SQLAlchemy
from main import bcrypt                                                      # Import the hasing package from main
from flask_jwt_extended import create_access_token                           # Package for providing JWTs
from datetime import timedelta                                               # Function to calculate the difference in time
from flask import Blueprint, request, jsonify, abort                         # Import flask and various sub packages

user = Blueprint('user', __name__, url_prefix="/user")                       # Creating the user blueprint, registered in __init__.py

@user.route("/register", methods=["POST"])                                   # Register route
def user_register():
    user_fields = user_schema.load(request.json)                             # Getting the fields from the User Schema
    user = User.query.filter_by(email=user_fields["email"]).first()       # Query the user table with the email and return the first user
    
    if user:                                                                 # If a user is returned 
        return abort(400, description="Email already in use")                # Return the error "Email already in use"

    user = User()                                                            # Re-init user as a new instance of the User model

    user.email = user_fields["email"]                                        # Add email to the user
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8") # Hash the password and add it to the user

    db.session.add(user)                                                     # Add the user to the db session
    db.session.commit()                                                      # Commit the session

    return jsonify(user_schema.dump(user))                                # Return the user that was just created


@user.route("/login", methods=["POST"])                                                             # Login route
def user_login():
    user_fields = user_schema.load(request.json)                                              # Getting the fields from the User Schema
    user = User.query.filter_by(email=user_fields["email"]).first()                        # Query the user table with the email and return the first user

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]): # If there is no user or the password is wrong
        return abort(401, description="Incorrect username or password")                             # Return the error "Incorrect username or password"

    expiry = timedelta(days=1)                                                                      # Time for the token to expire
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)              # The access token, with the user id and the expiration date

    return jsonify({ "token": access_token })                                                       # Return the token