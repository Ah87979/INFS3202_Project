import sys
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db

from resources.owner import OwnerListResource
from resources.vehicle import VehicleListResource, VehicleResource, VehicleRegisterResource


def create_app():
    print("Hello", file=sys.stderr)
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(OwnerListResource, '/owners')
    api.add_resource(VehicleListResource, '/vehicles')
    api.add_resource(VehicleResource, '/vehicles/<int:recipe_id>')
    api.add_resource(VehicleRegisterResource, '/vehicles/<int:vehicle_id>/register')


if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
