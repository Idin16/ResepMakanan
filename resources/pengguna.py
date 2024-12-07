from flask_restful import Resource
from db import mysql
from flask import jsonify, request, make_response
from .import services

class Pengguna(Resource):
    def get(self):     
        cursor = mysql.connection.cursor()
        cursor.execute("CALL LihatPengguna")
        
        data = cursor.fetchall()
        data = services.cursor_to_json(cursor, data)
        
        return jsonify({'message': 'success', 'Pengguna': data})

    def post(self):
        data = request.json
        nama = data.get('nama')
        namaemail = data.get('email')
        privatepassword = data.get('password')

        # Memanggil Prosedur
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("CALL RegisterPengguna(%s,%s,%s)", (nama,namaemail,privatepassword))
        except Exception as e:
            error_message = str(e)
            if 'Resep tidak ditemukan' in error_message:
                return jsonify({'message': f'Username {nama} sudah digunakan.'})
            elif 'Pengguna tidak ditemukan' in error_message:
                return jsonify({'message': f'Email {namaemail} sudah digunakan.'})
            else:
                return jsonify({'message': 'SystemError'})

        return jsonify({'message': f'Selamat! Akun {nama} berhasil dibuat'})
    
    def delete(self):
        data = request.json
        pengguna = data.get('nama_pengguna')

        if not  pengguna:
            return jsonify({'message': 'Nama pengguna tidak boleh kosong'})
        
        # Memanggil Prosdeur
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("CALL MenghapusPengguna(%s)", (pengguna, ))
        except Exception as e:
            error_message = str(e)
            if 'Pengguna tidak ditemukan' in error_message:
                return jsonify({'message': f'Pengguna {pengguna} tidak ditemukan.'})
            else:
                return jsonify({'message': 'SystemError'})

        cursor.close()

        return jsonify({'message': f'Pengguna {pengguna} berhasil dihapus'})