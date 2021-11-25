# terima input berupa bilangan bulat 
num_input = int(input("Silahkan masukkan angka berapapun : "))

# kuadratkan input pengguna
num_input_squared = num_input ** 2

# cetak hasilnya
output_msg = "Kuadrat dari {num_input} = {num_input_squared}".format(
    num_input=num_input, num_input_squared=num_input_squared)
# output_msg = "Kuadrat dari " + str(num_input) + " = " + str(num_input_squared)
print(output_msg)