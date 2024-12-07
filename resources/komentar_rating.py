from flask_restful import Resource
from db import mysql
from flask import jsonify, request, make_response
from .import services

class KomentarRating(Resource):
    def get(self):
        
        return
    

    def post(self):
        data = request.json
        nama = data.get('nama_resep')
        pengguna = data.get('nama_pengguna')
        tekskomentar = data.get('komentar')
        nilairating = data.get('rating')

        # Memanggil Prosedur
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("CALL TambahKomentarDanRating(%s,%s,%s,%s)", (nama,pengguna,tekskomentar,nilairating))
        except Exception as e:
            error_message = str(e)
            if 'Resep tidak ditemukan' in error_message:
                return jsonify({'message': f'Resep {nama} tidak ditemukan.'})
            elif 'Pengguna tidak ditemukan' in error_message:
                return jsonify({'message': f'Pengguna {pengguna} tidak ditemukan.'})
            elif 'Anda sudah memberikan komentar untuk resep ini.' in error_message:
                return jsonify({'message': f'Anda sudah memberikan komentar untuk resep ini.'})
            elif 'Anda sudah memberikan rating untuk resep ini.' in error_message:
                return jsonify({'message': f'Anda sudah memberikan rating untuk resep ini.'})
            else:
                return jsonify({'message': 'SystemError'})

        return jsonify({'message': f'Komentar pada resep {nama} berhasil ditambahkan'})
    
    def delete(self):
        data = request.json
        nama = data.get('nama_resep')
        pengguna = data.get('nama_pengguna')

        if not nama or not pengguna:
            return jsonify({'message': 'Nama resep dan nama pengguna tidak boleh kosong'})
        
        # Memanggil Prosdeur
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("CALL MenghapusKomentarRating(%s,%s)", (nama, pengguna))
        except Exception as e:
            error_message = str(e)
            if 'Resep tidak ditemukan' in error_message:
                return jsonify({'message': f'Resep {nama} tidak ditemukan.'})
            elif 'Pengguna tidak ditemukan' in error_message:
                return jsonify({'message': f'Pengguna {pengguna} tidak ditemukan.'})
            else:
                return jsonify({'message': 'SystemError'})

        cursor.close()

        return jsonify({'message': f'Komentar dari {pengguna} di resep {nama} berhasil dihapus'})