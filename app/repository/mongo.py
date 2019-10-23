"""
Funcions for mongo
"""
import os
from pymongo import MongoClient
from app.food_profile.settings import MONGO_URL, MONGO_DATABASE

COLLECTION_NAME = 'profiles'

class MongoRepository(object):
    """
    Repository implementation
    """

    def __init__(self):
        client = MongoClient(MONGO_URL)
        self.db = client[MONGO_DATABASE].profiles

    def create(self, profile):
        """
        Insert content in the collection
        :param profile:
        """
        return self.db.profiles.insert_one(profile)

    def find_all(self, selector):
        """
        Recover all food profiles
        :return: list of food profiles
        """
        return self.db.profiles.find(selector)

    def find(self, selector):
        """
        Recover one food profile
        :return: a food profile
        """
        return self.db.profiles.find_one(selector)

    def update(self, selector, profile):
        """
        Update an existing profile.
        :param selector:
        :param profile:
        :return: records affected
        """
        return self.db.profiles.replace_one(selector, profile).modified_count

    def delete(self, selector):
        """
        Remove profile
        :param selector:
        """
        return self.db.profiles.remove(selector)
