import sys
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db

from resources.owner import OwnerListResource, OwnerResource
from resources.vehicle import VehicleListResource, VehicleResource
from resources.violation import ViolationListResource, ViolationResource


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

    api.add_resource(OwnerListResource, '/owner')
    api.add_resource(OwnerResource, '/owner/<int:owner_id>')
    api.add_resource(VehicleListResource, '/vehicle')
    api.add_resource(VehicleResource, '/vehicle/<int:vehicle_id>')
    api.add_resource(ViolationListResource, '/violation')
    api.add_resource(ViolationResource, '/violation/<int:violation_id>')


if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
