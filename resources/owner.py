import sys
from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.owner import Owner


class OwnerListResource(Resource):

    def get(self):
        data = Owner.get_all()

        if data is None:
            return {'message': 'owner not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK
    
    def post(self):
        json_data = request.get_json()

        name = json_data.get('name')
        address = json_data.get('address')
        phone = json_data.get('phone')
        license_no = json_data.get('license_no')

        if Owner.get_by_name(name):
            return {'message': 'name already used'}, HTTPStatus.BAD_REQUEST

        owner = Owner(
            name=name,
            address=address,
            phone=phone,
            license_no=license_no
        )

        owner.save()

        data = {
            'owner_id': owner.owner_id,
            'name': owner.name,
            'address': owner.address,
            'phone': owner.phone,
            'license_no': owner.license_no
        }

        return data, HTTPStatus.CREATED

class OwnerResource(Resource):

    def get(self, owner_id):
        owner = Owner.get_by_id(owner_id)

        if owner is None:
            return {'message': 'owner not found'}, HTTPStatus.NOT_FOUND

        return owner.data, HTTPStatus.OK