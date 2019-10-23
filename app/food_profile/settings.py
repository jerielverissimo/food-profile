"""
Application Settings
"""
from os import environ

MONGO_URL = environ.get('MONGODB_URL', 'mongodb://localhost:27017/')

MONGO_DATABASE = environ.get('MONGO_DATABASE', 'food-profiles')
