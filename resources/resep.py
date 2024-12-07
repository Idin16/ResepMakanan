from flask_restful import Resource
from db import mysql
from flask import jsonify, request, make_response
from . import services

class Resep(Resource):
    def get(self, tipe=None):
        if not tipe:
            nama = request.args.get("nama_resep")
            if nama:
                print(nama)
                # Memanggil Prosedur
                cursor = mysql.connection.cursor()
                cursor.execute("CALL MencariResep(%s)", (nama, ))
                
                data = cursor.fetchall()
                data = services.cursor_to_json(cursor, data)
                
                return jsonify({'message': 'success', 'Resep': data})
            
            else:
                # Memanggil Prosedur
                cursor = mysql.connection.cursor()
                cursor.execute("CALL LihatResep")

                data = cursor.fetchall()
                data = services.cursor_to_json(cursor, data)
                cursor.close()

                return jsonify({'message': 'success', 'Semua Resep': data})
        
        elif tipe == 'populer':
            # Memanggil Prosedur
            cursor = mysql.connection.cursor()
            cursor.execute("CALL ResepPopuler")

            data = cursor.fetchall()
            data = services.cursor_to_json(cursor, data)
            cursor.close()

            return jsonify({'message': 'success', 'Resep Populer': data})  

        else:
            return jsonify({'message': 'invalid parameter'})


    def post(self):
        data = request.json
        nama = data.get('nama_resep')
        deskripsi = data.get('deskripsi')
        waktumemasak = data.get('waktu_memasak')
        tingkatkesulitan = data.get('tingkat_kesulitan')
        namapengguna = data.get('pembuat')
        langkahmemasak = data.get('langkah_memasak')
        kuantitas = data.get('kuantitas_bahan')

        # Memanggil Prosedur
        cursor = mysql.connection.cursor()
        cursor.execute("CALL TambahResepBaru(%s,%s,%s,%s,%s,%s,%s)", (nama,deskripsi,waktumemasak,tingkatkesulitan,namapengguna,langkahmemasak,kuantitas))

        return jsonify({'message': f'Resep {nama} Berhasil Ditambahkan'})  
    
    def put(self, id, hal=None):
        if not hal:
            data = request.json
            nama = data.get('nama_resep')
            deskripsi = data.get('deskripsi')
            waktumemasak = data.get('waktu_memasak')
            tingkatkesulitan = data.get('tingkat_kesulitan')

            # Memanggil Prosdeur
            cursor = mysql.connection.cursor()
            cursor.execute("CALL UbahResep(%s,%s,%s,%s)", (nama, deskripsi, waktumemasak, tingkatkesulitan))

            return jsonify({'message': f'Deskripsi resep {nama} berhasil diubah'})
        
        elif hal == 'langkah':
            data = request.json
            nama = data.get('nama_resep')
            langkahmemasak = data.get('langkah_memasak')

            # Memanggil Prosdeur
            cursor = mysql.connection.cursor()
            cursor.execute("CALL UbahLangkahMemasak(%s,%s)", (nama, langkahmemasak))
            cursor.close()

            return jsonify({'message': f'Langkah memasak untuk resep {nama} berhasil diubah'})
        
        elif hal == 'bahan':
            data = request.json
            nama = data.get('nama_resep')
            bahanmasak = data.get('kuantitas')

            # Memanggil Prosdeur
            cursor = mysql.connection.cursor()
            cursor.execute("CALL UbahResepBahan(%s,%s)", (nama, bahanmasak))
            cursor.close()

            return jsonify({'message': f'Bahan memasak untuk resep {nama} berhasil diubah'})
        
        else:
            return jsonify({'message': 'invalid parameter'})
        
    def delete(self):
        data = request.json
        nama = data.get('nama_resep')

        # Memanggil Prosdeur
        cursor = mysql.connection.cursor()
        cursor.execute("CALL MenghapusResep(%s)", (nama, ))
        cursor.close()

        return jsonify({'message': f'Resep {nama} berhasil dihapus'})

