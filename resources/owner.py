from flask import request
from flask_restful import Resource
from http import HTTPStatus

from utils import hash_password
from models.owner import Owner


class OwnerListResource(Resource):
    def post(self):
        json_data = request.get_json()

        name = json_data.get('name')

        # Do not add the owner if the name is taken
        if Owner.get_by_name(name):
            return {'message': 'name already used'}, HTTPStatus.BAD_REQUEST

        owner = Owner(
            name=name
        )

        owner.save()

        data = {
            'owner_id': owner.owner_id,
            'name': owner.name
        }

        return data, HTTPStatus.CREATED
