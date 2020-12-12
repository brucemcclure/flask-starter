TODO

- Set up the .env file

### Steps to make this your own project

| Install step                         | command                                                       |
| ------------------------------------ | ------------------------------------------------------------- |
| Clone the repo ( https )             | `git clone https://github.com/brucemcclure/flask-starter.git` |
| Clone the repo ( ssh )               | `git clone git@github.com:brucemcclure/flask-starter.git`     |
| cd into said repo                    | `cd flask-starter`                                            |
| delete the git file                  | `rm -rf .git`                                                 |
| greate a new git file                | `git init`                                                    |
| create a new repo in your github     | `Create your repo up in GitHub`                               |
| push this project back up to it      | `Follow those steps setoput bu GitHub`                        |
| Smile because youre freaking amazing | `🦆`                                                          |

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

| Command              | Effect                                             |
| -------------------- | -------------------------------------------------- |
| flask db init        | Initilizes the app to use migrations               |
| flask db-custom drop | Drops all tables in the database                   |
| flask db upgrade     | Upgrades the database with the most recent changes |
| flask db-custom seed | Seeds the database                                 |
| flask db downgrade   | Downgrades the database to the previous changes    |

This project contains the following pip packages
NB This does not include their dependencies. Please see the requirements.txt

| package                                                                    | Use                                                      |
| -------------------------------------------------------------------------- | -------------------------------------------------------- |
| [Flask](https://flask.palletsprojects.com/en/1.1.x/)                       | Python Micro Framework                                   |
| [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)   | Integration layer for Flaks and Marshmallow              |
| [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) | Support for managing JWTs with flask                     |
| [bcrypt](https://pypi.org/project/bcrypt/)                                 | Good password hashing for your software and your servers |
| [SQLAlchemy](https://docs.sqlalchemy.org/en/13/orm/)                       | ORM                                                      |
| [boto3](https://pypi.org/project/boto3/)                                   | AWS python SDK                                           |
| [marshmallow](https://pypi.org/project/marshmallow/)                       | Used to convert complex datatypes to and from Python     |
| [Flask-Migrate](https://pypi.org/project/Flask-Migrate/)                   | SQLAlchemy DB migrations for Flask apps using Alembic    |
| [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)             | Adds support for SWLAlchemy for your flask app           |
| [marshmallow-sqlalchemy](https://pypi.org/project/marshmallow-sqlalchemy/) | Integration for SQLAlchemy and marshmallow               |
| [psycopg2](https://pypi.org/project/psycopg2/)                             | Postgres adapter for Python                              |

###### NB: if psycopg2 doent install then install psycopg2-binary `pip install psycopg2-binary`

Run tests with this -> `python -m unittest discover -s src/tests -v`

### Examples of relationships you should build

| Relationship | Example                                      |
| ------------ | -------------------------------------------- |
| one-to-one   | User has one Profile                         |
| one-to-many  | User has many Picures                        |
| Many-to-many | User has many Examples through examples_join |
