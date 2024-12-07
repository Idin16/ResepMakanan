from flask_restful import Resource
from db import mysql
from flask import jsonify, request, make_response
from .import services

class Pengguna(Resource):
    def get(self):
        return
    

    def post(self):
        # kode kalo post request
        return