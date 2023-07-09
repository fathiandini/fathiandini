from flask import Flask, render_template, request, redirect, url_for
import os
from database import getMySqlConnection
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/images'


@app.route("/")  # rute yang di akses di url
def index():  # fungsi yang dipanggil sesuai dengan url diatas
    db = getMySqlConnection()  # fungsi yang dipanggil sesuai dengan url diatas
    sqlstr = f"SELECT * from album"
    cur = db.cursor()
    cur.execute(sqlstr)
    output_json = cur.fetchall()
    print(output_json)
    return render_template('home.html', data=output_json)

@app.route("/detail/<int:id>")
def detail(id):
    db = getMySqlConnection()  # fungsi yang dipanggil sesuai dengan url diatas
    sqlstr = f"SELECT * from album where id = {id}"
    cur = db.cursor()
    cur.execute(sqlstr)
    output_json = cur.fetchall()
    print(output_json)
    return render_template('home.html', data=output_json)
@app.route("/delete/<int:id>")
def delete(id):
    db = getMySqlConnection()  # fungsi yang dipanggil sesuai dengan url diatas
    sqlstr = f"DELETE from album where id = {id}"
    cur = db.cursor()
    cur.execute(sqlstr)
    db.commit()
    cur.close()
    return redirect(url_for('index'))

# rute yang di akses di url


@app.route("/tambah_menu", methods=['POST', 'GET'])
def tambah_menu():  # fungsi yang dipanggil sesuai dengan url diatas
    db = getMySqlConnection()  # fungsi yang dipanggil sesuai dengan url diatas
    if request.method == "POST":
        data = request.form.to_dict()
        file = request.files['alamat_gambar']
        data['alamat_gambar'] = file.filename
        print(data)
        try:
            cur = db.cursor()
            sqlstr = f"INSERT INTO album (nama_album, deskripsi, alamat_gambar) VALUES('{data['nama_album']}', '{data['deskripsi']}', '{data['alamat_gambar']}')"
            cur.execute(sqlstr)
            db.commit()
            cur.close()
            file.save(os.path.join('static/images', file.filename))
            print('sukses')
            # output_json = cur.fetchall()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('index'))
    return render_template('add_menu.html')

@app.route("/update_album/<int:id>", methods=['POST', 'GET'])
def update_album(id):  # fungsi yang dipanggil sesuai dengan url diatas
    db = getMySqlConnection()

    if request.method == "POST":
        data = request.form.to_dict()  # ambil data dari form

        gambarAlbum = request.files['gambar_album']  # ambil data gambar

        try:
            cur = db.cursor()

            if gambarAlbum.filename:  # jika gambar di update
                print("true")

                # update nama gambar di database
                cur.execute(
                    f"UPDATE album SET alamat_gambar = '{gambarAlbum.filename}'WHERE id = {id}")
                db.commit()

                # save gambar di folder images
                gambarAlbum.save(os.path.join(
                    'static/images', gambarAlbum.filename))

            sqlstr = f"UPDATE album SET nama_album = '{data['nama_album']}', deskripsi = '{data['deskripsi']}' WHERE id = {id}; "

            cur.execute(sqlstr)

            db.commit()
            cur.close()

            print('sukses')
            print(data)
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return redirect(url_for('index'))

    else:
        sqlstr = f"SELECT * from album where id = {id}"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()

        print(output_json)
        return render_template('update_form.html', data=output_json)


@app.route("/about")
def about_page():
    return render_template('about.html', title='ini judul', message='pesan di halaman about')


@app.route("/product/<int:product_id>")
def show_product(product_id):
    return f"product id: {product_id}"


if __name__ == "__main__":
    app.run(debug=True)
