

from ast import operator


x = 1  # angka 1 atau desimal adalah tipe integer

pi = 3.14  # ini adalah float

str_pi = "3.14"  # ini adalah string

boolean = False  # ini

print(type(pi))

##################################

groceries = ["apel", "pisang", "jeruk"]
# index dalam list dimulai dari 0

peserta = ("joko", "daffa")

dictionary = {
    "nama": "surya",
    "umur": 15,
    'kota': 'depok'
}

# print(type(groceries))
# print(type(peserta))
# print(type(dictionary))


# print(groceries[1]) #cara memanggil elemen dengan menggunakan []
# print(dictionary["kota"])

######################################
# opearator aritmatika

# print(2 + 3)
# print(5 - 3)
# print(3 * 4)
# print(4 / 2)
# print(5 % 2)
# print(2 ** 3)

###################################

x = 3

print(x + 3)

print(f'tanpa assignment operator: {x}')

x += 3
print(f'dengan assignment operator: {x}')
###################################
# operator perbandingan

# print(5 == 5)
# print(5 > 2)
# print(5 != 5)
# print(5 < 4)
# print(5 >= 5)
# print(5 > 5)
####################################
# operator logika

print(5 < 7 and 5 > 3)  # true
print(5 > 7 and 5 > 3)  # salah satu bernilai False akan mengembalikan false

print(5 < 7 or 5 > 3)  # true
print(5 > 7 or 5 > 3)  # false

print(not(5 > 7 or 5 > 3))  # false
