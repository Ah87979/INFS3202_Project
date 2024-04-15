from flask import request
from flask_restful import Resource
from http import HTTPStatus

from utils import hash_password
from models.violation import Violation

class ViolationListResource(Resource):

    def get(self):
        data = Violation.get_all()

        if data is None:
            return {'message': 'violation not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK

class ViolationResource(Resource):

    def get(self, violation_id):
        violation = Violation.get_by_id(violation_id)

        if violation is None:
            return {'message': 'violation not found'}, HTTPStatus.NOT_FOUND

        return violation.data, HTTPStatus.OK