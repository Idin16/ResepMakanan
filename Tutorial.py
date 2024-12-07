from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sistem_manajemen_resep_makanan'

mysql = MySQL(app)


# Resep
@app.route('/resep', methods=['GET', 'POST', 'PUT', 'DELETE'])
def resep():
    if request.method == 'POST':
        data = request.json
        resep = data.get('resep')
        query = "INSERT INTO resep(nama, deskripsi, waktu_memasak, tingakt_kesulitan, id_pengguna) VALUES (%s, %s, %s, %s, %s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (resep, ))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'ijat gay'})
    
    elif request.method == 'GET':
        query = "SELECT * FROM resep"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{'id_resep': row[0], 'nama': row[1], 'deskripsi': row[2], 'waktu_memasak': row[3], 'tingkat_kesulitan': row[4], 'id_pengguna': row[5]} for row in data]
        cursor.close()

        return jsonify({'message': 'success', 'data': data})
    
    elif request.method == 'PUT':
        data = request.json
        nama = data.get('nama')
        deskripsi = data.get('deskripsi')
        waktu_memasak = data.get('waktu_memasak')
        tingkat_kesulitan = data.get('tingkat_kesulitan')

        query = "UPDATE buku SET nama = %s, deskripsi = %s, waktu_memasak = %s, tingkat_kesulitan = %s WHERE id_resep = %s"

        cursor = mysql.connection.cursor()
        cursor.execute(query, (nama, deskripsi, waktu_memasak, tingkat_kesulitan, id))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'success'})
    
    elif request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM resep WHERE id_resep = %s", (id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'success'})

# Langkah_memasak
@app.route('/langkah_memasak', methods=['GET', 'POST', 'PUT'])
def langkah_memasak():
    if request.method == 'POST':
        data = request.json
        langkah = data.get('langkah_memasak')
        query = "INSERT INTO deskripsi(langkah_memasak) VALUES (%s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (langkah, ))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'ijat gay'})
    
    elif request.method == 'GET':
        query = "SELECT * FROM langkah_memask"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{'id_langkah': row[0], 'id_resep': row[1], 'deskripsi': row[2]} for row in data]
        cursor.close()

        return jsonify({'message': 'success', 'data': data})
    
    elif request.method == 'PUT':
        data = request.json
        deskripsi = data.get('deskripsi')

        query = "UPDATE langkah_memasak SET deskripsi = %s WHERE id_resep = %s"

        cursor = mysql.connection.cursor()
        cursor.execute(query, (deskripsi, id))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'success'})

# Resep_bahan
@app.route('/resep_bahan', methods=['GET', 'POST', 'PUT'])
def resep_bahan():
    if request.method == 'POST':
        data = request.json
        kuantitas = data.get('kuantitas')
        query = "INSERT INTO resep_bahan(kuantitas) VALUES (%s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (kuantitas, ))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'ijat gay'})
    
    elif request.method == 'GET':
        query = "SELECT * FROM resep_bahan"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{'id_resep': row[0], 'kuantitas': row[1]} for row in data]
        cursor.close()

        return jsonify({'message': 'success', 'data': data})
    
    elif request.method == 'PUT':
        data = request.json
        kuantitas = data.get('kuantitas')

        query = "UPDATE rsep_bahan SET kuantitas = %s WHERE id_resep = %s"

        cursor = mysql.connection.cursor()
        cursor.execute(query, (kuantitas, id))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'success'})

# Komentar
@app.route('/komentar', methods=['GET', 'POST', 'DELETE'])
def komentar():
    if request.method == 'POST':
        data = request.json
        komentar = data.get('teks_komentar')
        query = "INSERT INTO komentar(teks_komentar) VALUES (%s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (komentar, ))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'ijat gay'})

    elif request.method == 'GET':
        query = "SELECT * FROM komentar"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{'id_komentar': row[0], 'id_resep': row[1], 'id_pengguna': row[2], 'teks_komentar': row [3], 'tanggal': row[4]} for row in data]
        cursor.close()

        return jsonify({'message': 'success', 'data': data})
    
    elif request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM komentar WHERE id_komentar = %s", (id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'success'})

# Pengguna
@app.route('/pengguna', methods=['GET', 'POST', 'DELETE'])
def pengguna():
    if request.method == 'POST':
        data = request.json
        pengguna = data.get('pengguna')
        query = "INSERT INTO resep(nama, email, private_password) VALUES (%s, %s, %s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (pengguna, ))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'success'})
    
    elif request.method == 'GET':
        query = "SELECT * FROM pengguna"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{'id_pengguna': row[0], 'nama': row[1], 'email': row[2], 'private_password': row[3], 'id_role': row[4]} for row in data]
        cursor.close()

        return jsonify({'message': 'success', 'data': data})
    
    elif request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM pengguna WHERE id_pengguna = %s", (id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'success'})

# Rating
@app.route('/rating', methods=['GET', 'POST', 'DELETE'])
def rating():
    if request.method == 'POST':
        data = request.json
        rating = data.get('rating')
        query = "INSERT INTO rating(id_resep, id_pengguna, nilai_rating) VALUES (%s, %s, %s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (rating, ))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'message': 'success'})
    
    elif request.method == 'GET':
        query = "SELECT * FROM rating"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{'id_rating': row[0], 'id_resep': row[1], 'id_pengguna': row[2], 'nilai_rating': row[3], 'tanggal': row[4]} for row in data]
        cursor.close()

        return jsonify({'message': 'success', 'data': data})
    
    elif request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM rating WHERE id_rating = %s", (id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'success'})
    

if __name__ == '__main__':
    app.run(debug=True)