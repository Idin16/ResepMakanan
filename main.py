from flask import Flask, jsonify, request
from flask_restful import Api
from db import mysql

from resources.resep import Resep
from resources.komentar_rating import KomentarRating
from resources.pengguna import Pengguna

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'resep_makanan'

mysql.init_app(app)

api.add_resource(Resep, '/resep', '/resep/<string:tipe>', '/resep/<int:id>','/resep/<int:id>/<string:hal>')
api.add_resource(KomentarRating, '/komentar')
api.add_resource(Pengguna, '/pengguna')

if __name__ == '__main__':
    app.run(debug=True)