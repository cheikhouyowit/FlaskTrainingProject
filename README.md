# Testing

Branch: testing

Summary: This branch sets up testing for your Flask application, ensuring your code works as expected and catching errors early.

Key Concepts:

    Unit testing with pytest and pytest-flask.
    Writing test cases for different parts of your application.

Example Code:

import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()
    
    with app.app_context():
        db.create_all()
    
    yield client

# Steps:
1. Install pytest and pytest-flask.
2. Set up test configuration in conftest.py.
3. Write test cases in test_app.py.
4. Run tests using pytest.
