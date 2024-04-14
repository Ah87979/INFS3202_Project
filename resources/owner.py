from flask import request
from flask_restful import Resource
from http import HTTPStatus

from utils import hash_password
from models.owner import Owner


class OwnerListResource(Resource):
    def post(self):
        json_data = request.get_json()

        name = json_data.get('name')
        # email = json_data.get('email')
        # non_hash_password = json_data.get('password')

        # Do not add the owner if the name is taken
        if Owner.get_by_name(name):
            return {'message': 'name already used'}, HTTPStatus.BAD_REQUEST

        # Do not add the owner if the email is taken
        # if Owner.get_by_email(email):
        #     return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        # password = hash_password(non_hash_password)

        owner = Owner(
            name=name
        )

        owner.save()

        data = {
            'owner_id': owner.owner_id,
            'name': owner.name,
            # 'email': owner.email
        }

        return data, HTTPStatus.CREATED
