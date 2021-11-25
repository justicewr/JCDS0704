# 485 hari = 1 tahun + 4 bulan + 0 minggu + 5 hari 

days_input = int(input("Masukkan jumlah hari: "))
days_per_year = 360
days_per_month = 30
days_per_week = 7

total_year = days_input // days_per_year # hasil floor division
year_remainder = days_input % days_per_year # hasil modulo

# TODO: continue similar operations
# total_month
# total_week 
# total_day

print(year_remainder)
# 485 hari --> 1,sekian tahun