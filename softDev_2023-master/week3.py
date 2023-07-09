######### kondisional ###############
from sympy import true


x = 2

# jika kondisi true makan kode akan di jalankan
# if x > 5:
#     print("Nilai x lebih besar dari 5")


##############################

# jika kondisi if salah maka akan menjalankan kode else
# if x > 5:
#     print('nilai x lebih besar dari 5')
# else:
#     print('nilai x lebih kecil dari 5')

############################


# if x > 7:
#     print('nilai x lebih besar dari 7')
# elif x > 5:
#     print('nilai x lebih besar dari 5')
# else:
#     print('nilai x lebih kecil dari 5')


# perulangan

# numbers = [1, 2, 3, 4, 5]

# for angka in numbers:
#     print(angka)

# for huruf in 'yusuf':
#     print(huruf)

# for i in range(6): #range(n-1)
#     print(i)
# print("\n")
# for j in range(2, 6):
#     print(j)

# print("\n")

# for i in range(6):
#     print('yusuf')

# nested loop
# angkaPrimer = [0,1,2,3]
# angkaSekunder = [4,5,6,7]

# for luar in angkaPrimer:
#     for dalam in angkaSekunder:
#         print(luar, dalam)
#     print('\n')

# while loop
# index = 0
# murid = ['a', 'b', 'c']
# # len() untuk cek berapa banyak elemen

# while index <= len(murid) - 1:
#     print(murid[index])
#     index += 1  # 2 3

# for i in range(len(murid)):
#     print(murid[i])

# while True:
#     print('yusuf')
#     angka = int(input('masukkan angka: '))
#     if angka == 1:
#         break


i = 0
while i < 6:
    i += 1 #1
    if i == 3:
        continue
    print(i)

print('\n')

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)