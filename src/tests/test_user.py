import unittest                                                         # This is the inbuilt python testing module
from main import create_app, db                                         # This is the create_app function from the factory pattern and the DB from main
from models.User import User                                      # The User module to be used to log in to retrieve a JWT

class TestProfiles(unittest.TestCase):                                  # This is the Parent class that will test our Profile functionality.    
    @classmethod
    def setUp(cls):                                                     # This method will run before each and every class
        cls.app = create_app()                                          # Create a new instance of app
        cls.app_context = cls.app.app_context()                         # Creating context for which the app is in. The tests run in parrallel therefore we need to keep track of which instance of app we are using
        cls.app_context.push()                                          # Pushing context. Read the docs for more
        cls.client = cls.app.test_client()                              # Adding the test client to the client
        db.create_all()                                                 # Create all the 
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])                       # This seeds the db

    @classmethod                                                        # This method will run after each and every class
    def tearDown(cls):                                                  # We want to delete all the data from the class tests
        db.session.remove()                                             # Remove the session from the db
        db.drop_all()                                                   # Drop all tables
        cls.app_context.pop()                                           # Remove the context of the app


    def test_user_register(self):
        response = self.client.post("/user/register",                   # Sending a post request to /user/register
        json = {                                                        # Data needed to register a new user
            "email": "test6@test.com",
            "password": "123456"
        })
        self.assertEqual(response.status_code, 200)                     # Make sure the status codefrom the response is 200
        data = response.get_json()                                      # Convert the data to JSON

        response = self.client.post("/user/login",                      # Sending a post request to /user/login
        json = {                                                        # The json data needed to login ( From the new user )
            "email": "test6@test.com",
            "password": "123456"
        })                    
        data = response.get_json()                                      # jsonify the data
        self.assertEqual(response.status_code, 200)                     # Checking if the response code is 200 you can make it a range 200-299 too


    def test_user_login(self):
        response = self.client.post("/user/login",                       # Sending a post request to /user/login
        json = {                                                         # The json data needed to login
            "email": "test1@test.com",
            "password": "123456"
        })
        data = response.get_json()                                        # Convert the response to data
        self.assertEqual(response.status_code, 200)                       # Checking if the response code is 200 you can make it a range 200-299 too
        self.assertIsInstance(data['token'], str)                         # Checking the data data type of the token
