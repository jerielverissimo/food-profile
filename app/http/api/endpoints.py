from flask import Flask, json, g, request
from app.food_profile.service import Service as ProfileService
from app.food_profile.schema import FoodProfileSchema
import uuid

app = Flask(__name__)

@app.route('/profiles', methods=['GET'])
def index():
    return json_response(ProfileService().find_all_profiles())

@app.route('/profiles', methods=['POST'])
def create():
    payload = FoodProfileSchema().load(json.loads(request.data))

    profile_id = uuid.uuid4()
    profile = ProfileService(profile_id).create_profile_for(payload)
    return json_response(profile)

@app.route('/profile/<string:profile_id>', methods=['GET'])
def show(profile_id):
    profile = ProfileService(uuid.UUID(profile_id)).find_profile()

    if profile:
        return json_response(profile)
    else:
        return json_response({'error': 'profile not found for id: ' + profile_id}, 404)

@app.route('/profile/<string:profile_id>', methods=['PUT'])
def update(profile_id):
    req_profile = FoodProfileSchema().load(json.loads(request.data))

    profile_service = ProfileService(uuid.UUID(profile_id))

    if profile_service.update_profile_with(req_profile):
        return json_response(req_profile)
    else:
        return json_response({'error': 'profile not found'}, 404)

@app.route('/profile/<string:profile_id>', methods=['DELETE'])
def delete(profile_id):
    p_id = uuid.UUID(profile_id)
    profile_service = ProfileService(p_id)

    if profile_service.delete_profile_for(p_id):
        return json_response({})
    else:
        return json_response({'error': 'profile not found'}, 404)


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})
