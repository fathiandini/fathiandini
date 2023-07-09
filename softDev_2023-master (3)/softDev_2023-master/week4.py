
def cek_genap_list(angka):
    for i in angka:  # looping untuk cek setiap angka di dalam list
        if i % 2 == 0:
            print('genap')
        else:
            print('ganjil')


def cek_genap():
    # input yang kita masukkan tipe data default nya adalah string
    # untuk mengubah menjadi integer bisa menggunakan fungsi int()
    # bisa baca di w3school tentang type casting
    angka = int(input(('masukkan angka: ')))
    if angka % 2 == 0:
        print('genap')
    else:
        print('ganjil')


def fungsi_salam(nama, divisi):  # nama parameter tidak bisa diawali dengan angka
    print(f'hallo nama saya {nama} dari divisi {divisi}')


def hitung(angka1, angka2):
    hasil = angka1 + angka2
    print(hasil)


def list_buah(fruits):
    for fruit in fruits:
        print(fruit)


fungsi_salam('john', 4)
print("\n")
hitung(4, 7)
print("\n")

fruits = ['apel', 'mangga', 'pisang']
list_buah(fruits)
print("\n")

cek_genap_list()([4, 5, 6, 7, 8, 9, 13])
