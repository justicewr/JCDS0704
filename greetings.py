# Program untuk memperkenalkan diri berdasarkan nama, usia, dan asal pengguna

# 1. Terima input (masukan) berupa nama, usia, dan asal pengguna
my_name = input("Masukkan nama Anda: ")
my_age = input("Masukkan usia Anda (angka saja): ")
my_address = input("Masukkan alamat Anda: ")

# 2. Siapkan pesan yang akan dicetak
message = "Nama saya {name}, usia saya {age} tahun. Saya dari {place}.".format(
    name=my_name, age=my_age, place=my_address)

# 3. Cetak pesan
print(message)