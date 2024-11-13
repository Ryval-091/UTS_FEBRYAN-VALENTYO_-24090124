A = int(input(f"masukkan nilai A : "))
B = int(input(f"masukkan nilai B : "))

pilih = input(f'pilih operasi : 1. penjumlahan/2. pengurangan/3. perkalian')

if pilih == '1' or 'penjumlahan':
    print(f"hasil operasi A + B : {A + B}") 

elif pilih == '2' or 'pengurangan':
    print(f"hasil operasi A - B : {A - B}") 

elif pilih == '3'or 'perkalian':
    print(f"hasil operasi A * B : {A * B}") 