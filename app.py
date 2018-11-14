from flask import Blueprint
from flask_restful import Api, Resource
from resources.jadwal import Jadwal

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class Hello(Resource):
    def get(self):
        return {'status':'ok'}

api.add_resource(Hello, '/')
api.add_resource(Jadwal, '/jadwal/<string:hari>/<string:sesi>')
