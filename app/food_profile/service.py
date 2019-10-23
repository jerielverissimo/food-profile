from ..repository.mongo import MongoRepository
from .schema import FoodProfileSchema

class Service(object):
    def __init__(self, profile_id=None, repo_client=MongoRepository()):
        self.repo_client = repo_client
        self.profile_id = profile_id

    def create_profile_for(self, food):
        self.repo_client.create(self.__prepare_profile(food))
        return self.__dump(food)

    def find_all_profiles(self):
        profiles = self.repo_client.find_all({})
        return [self.__dump(profile) for profile in profiles]

    def find_profile(self):
        profile = self.repo_client.find({'profile_id': self.profile_id})
        return self.__dump(profile)

    def update_profile_with(self, profile):
        records_affected = self.repo_client.update({'profile_id': self.profile_id}, self.__prepare_profile(profile))
        return records_affected > 0

    def delete_profile_for(self, profile_id):
        return self.repo_client.delete({'profile_id': profile_id})

    def __dump(self, data):
        return FoodProfileSchema().dump(data)

    def __prepare_profile(self, profile):
        data = profile
        data['profile_id'] = self.profile_id
        return data
