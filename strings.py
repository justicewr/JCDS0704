speech = 'He says, \'Good morning.\''

full_name = '''Idris\nIzzaturrahman'''

# print(full_name)
# full_name = '''
# Idris""''""''
# Izzaturrahman
# '''

# full_name = "idris izzaturrahman Haidar"
# print(full_name.split(" "))

capital = "DKI Jakarta" # K: huruf kedua, ada di indeks ke-1

# print(capital[-7])


# indexing --> starts with 0

# DKI Jakarta (11 karakter)
# 0 -11 D 
# 1 -10 K 
# 2 -9 I 
# 3 -8 
# 4 -7 J 
# 5 -6 a 
# 6 -5 k 
# 7 -4 a 
# 8 -3 r 
# 9 -2 t 
# 10 -1 a 

# capital = 'DKI Jakarta' # rentang indeks: 0 - 10  atau -11 - -1
# ambil DKI 

# print(capital[-3:]) # capital[8:]
# print(len(capital[:-7])) # capital[:4]
# print(capital[-13]) # capital[1:8]
# print(capital[1:4])

# my_int = 100

# print(capital + " " + str(my_int))

# my_name = "Idris"
# my_age = 25
# my_address = "Bekasi"

# message = "Nama saya " + my_name + ", usia saya " + str(my_age) + " tahun."
# message = "Nama saya {name}, usia saya {age} tahun.".format(age=25, name="Idris")

# terima input berupa nama, usia, dan asal pengguna
my_name = 
my_age = 
my_address = 

message = "Nama saya {name}, usia saya {age} tahun. Saya dari {place}.".format(
    place=my_address, age=my_age, name=my_name)

print(message)