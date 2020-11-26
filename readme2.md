TODO

Must change the profile view to check JWT

### Commands to set up the db

| Install step                           | command                                                 |
| -------------------------------------- | ------------------------------------------------------- |
| Update package information             | `sudo apt update`                                       |
| Install postgres                       | `sudo apt install postgresql`                           |
| Change user to postgres                | `sudo -i -u postgres`                                   |
| Open the Postgres console              | `psql`                                                  |
| Create the database                    | `CREATE DATABASE {db_name};`                            |
| Create user                            | `CREATE USER {user};`                                   |
| Give full privalages to the admin user | `grant all privileges on database {db_name} to {user};` |
| change password for user               | `ALTER USER {user} WITH ENCRYPTED PASSWORD '{password}` |

### Commands to interact with db

flask db-custom drop drops the database
flask db upgrade resets the database with the most recent migrations
flask db-custom seed seeds the database

| Command              | Effect                                             |
| -------------------- | -------------------------------------------------- |
| flask db init        | Initilizes the app to use migrations               |
| flask db-custom drop | Drops all tables in the database                   |
| flask db upgrade     | Upgrades the database with the most recent changes |
| flask db-custom seed | Seeds the database                                 |
| flask db downgrade   | Downgrades the database to the previous changes    |

This project contains the following pip packages
NB This does not include their dependencies. Please see the requirements.txt

| package                | Use                                                      | Link to docs                                         |
| ---------------------- | -------------------------------------------------------- | ---------------------------------------------------- |
| Flask                  | Python Micro Framework                                   | https://flask.palletsprojects.com/en/1.1.x/          |
| flask-marshmallow      | Integration layer for Flaks and Marshmallow              | https://flask-marshmallow.readthedocs.io/en/latest/  |
| Flask-JWT-Extended     | Support for managing JWTs with flask                     | https://flask-jwt-extended.readthedocs.io/en/stable/ |
| bcrypt                 | Good password hashing for your software and your servers |                                                      |
| SQLAlchemy             | ORM                                                      |                                                      |
| boto3                  | AWS python SDK                                           |                                                      |
| marshmallow            | used to convert complex datatypes to and from Python     |                                                      |
| Flask-Migrate          | SQLAlchemy DB migrations for Flask apps using Alembic    |                                                      |
| Flask-SQLAlchemy       | Adds support for SWLAlchemy for your flask app           |                                                      |
| marshmallow-sqlalchemy | Integration for SQLAlchemy and marshmallow               |                                                      |
| psycopg2-binary        | Postgres adapter for Python                              |                                                      |

`python -m unittest discover -s src/tests -v`
