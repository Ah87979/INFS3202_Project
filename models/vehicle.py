import sys
from extensions import db
from resources.owner import OwnerListResource
from models.owner import Owner
from http import HTTPStatus


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    vehicle_id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(200), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    registration_date = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    
    owner_id = db.Column(db.Integer(), db.ForeignKey("owner_id"))

    @property
    def data(self):
        return {
            'vehicle_id': self.vehicle_id,
            'manufacturer': self.manufacturer,
            'model': self.model,
            'year': self.year,
            'registration_date': self.registration_date,
            'Owner': Owner.get_name_by_id(self.owner_id)
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()

        result = []

        for i in r:
            result.append(i.data)

        return result

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.id == id).first()
    
    @classmethod
    def get_by_id_n(cls, id):
        x = cls.query.filter(cls.id == id).first()
        return x

    @classmethod
    def update(cls, id, data):
        vehicle = cls.query.filter(cls.id == id).first()

        if vehicle is None:
            return {'message': 'vehicle not found'}, HTTPStatus.NOT_FOUND

        vehicle.vehicle_id = data['vehicle_id']
        vehicle.manufacturer = data['manufacturer']
        vehicle.model = data['model']
        vehicle.year = data['year']
        vehicle.registration_date = data['registration_date']
        db.session.commit()
        return vehicle.data, HTTPStatus.OK

    @classmethod
    def delete(cls, id):
        vehicle = cls.query.filter(cls.id == id).first()
        if vehicle is None:
            return {'message': 'vehicle not found'}, HTTPStatus.NOT_FOUND

        db.session.delete(vehicle)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT
