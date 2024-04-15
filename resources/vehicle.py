import sys
from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.vehicle import Vehicle


class VehicleListResource(Resource):

    def get(self):
        data = Vehicle.get_all()

        if data is None:
            return {'message': 'vehicle not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        vehicle = Vehicle(
            vehicle_id=data['vehicle_id'],
            manufacturer=data['manufacturer'],
            model=data['model'],
            year=data['year'],
            owner_id=data['owner_id']
        )
        vehicle.save()

        return vehicle.data, HTTPStatus.CREATED


class VehicleResource(Resource):

    def get(self, vehicle_id):
        vehicle = Vehicle.get_by_id(vehicle_id)

        if vehicle is None:
            return {'message': 'vehicle not found'}, HTTPStatus.NOT_FOUND

        return vehicle.data, HTTPStatus.OK

    def put(self, vehicle_id):
        data = request.get_json()

        return Vehicle.update(vehicle_id, data)

    def delete(self, vehicle_id):
        return Vehicle.delete(vehicle_id)