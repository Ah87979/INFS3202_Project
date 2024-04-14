import sys
from extensions import db
from resources.owner import OwnerListResource
from models.owner import Owner
from http import HTTPStatus


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    vehicle_id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(200))
    year = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    directions = db.Column(db.String(1000))
    is_register = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    owner_id = db.Column(db.Integer(), db.ForeignKey("owner.id"))

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num_of_servings': self.num_of_servings,
            'cook_time': self.cook_time,
            'directions': self.directions,
            'Owner': Owner.get_name_by_id(self.owner_id)
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.filter_by(is_publish=True).all()

        result = []

        for i in r:
            result.append(i.data)

        return result

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter((cls.id == id) & (cls.is_publish == True)).first()
    
    @classmethod
    def get_by_id_n(cls, id):
        x = cls.query.filter((cls.id == id) & (cls.is_publish == False)).first()
        return x

    @classmethod
    def update(cls, id, data):
        vehicle = cls.query.filter(cls.id == id).first()

        if vehicle is None:
            return {'message': 'vehicle not found'}, HTTPStatus.NOT_FOUND

        vehicle.name = data['name']
        vehicle.description = data['description']
        vehicle.num_of_servings = data['num_of_servings']
        vehicle.cook_time = data['cook_time']
        vehicle.directions = data['directions']
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

    @classmethod
    def publish(cls, vehicle_id):
        vehicle = Vehicle.get_by_id_n(vehicle_id)
        if vehicle is None:
            return {'message': 'vehicle not found'}, HTTPStatus.NOT_FOUND

        vehicle.is_publish = True
        db.session.commit()
        return vehicle.data, HTTPStatus.OK

    @classmethod
    def un_publish(cls, vehicle_id):
        vehicle = Vehicle.get_by_id(vehicle_id)
        if vehicle is None:
            return {'message': 'vehicle not found'}, HTTPStatus.NOT_FOUND

        vehicle.is_publish = False
        db.session.commit()
        return vehicle.data, HTTPStatus.OK
