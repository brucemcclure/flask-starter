TODO

Must change the profile view to check JWT

### Commands to set up the db

sudo -i -u postgres
createdb database_name
createuser name_of_user_to_administer_db

psql
grant all privileges on database database_name to name_of_user_to_administer_db;
alter user app with encrypted password 'a pretty good password';

### Commands to interact with db

flask db-custom drop drops the database
flask db upgrade resets the database with the most recent migrations
flask db-custom seed seeds the database

| Command                   | Effect                                              |
| ------------------------- | --------------------------------------------------- |
| flask db-custom drop      | drops the database                                  |
| flask db upgrade          | resets the database with the most recent migrations |
| flask db-custom seed      | seeds the database                                  |
| flask db-custom downgrade | rolls back the database                             |

This project contains the following pip packages
NB This does not include their dependencies. Please see the requirements.txt

| package                | Use                                                      |
| ---------------------- | -------------------------------------------------------- |
| Flask                  | Python Micro Framework                                   |
| flask-marshmallow      | Integration layer for Flaks and Marshmallow              |
| Flask-JWT-Extended     | Support for managing JWTs with flask                     |
| bcrypt                 | Good password hashing for your software and your servers |
| SQLAlchemy             | ORM                                                      |
| boto3                  | AWS python SDK                                           |
| marshmallow            | used to convert complex datatypes to and from Python     |
| Flask-Migrate          | SQLAlchemy DB migrations for Flask apps using Alembic    |
| Flask-SQLAlchemy       | Adds support for SWLAlchemy for your flask app           |
| marshmallow-sqlalchemy | Integration for SQLAlchemy and marshmallow               |
| psycopg2-binary        | Postgres adapter for Python                              |

`python -m unittest discover -s src/tests -v`
