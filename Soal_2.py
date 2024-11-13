tahun =int(input(f"Masukkan Tahun : "))
tahunkabisat = tahun / 400
tahunkabisat1 = tahun / 4
tahunkabisat2 = tahun / 100

if tahunkabisat == 0 : 
    print(f'Tahun {tahun} merupakan TAHUN KABISAT')
elif (tahunkabisat1 == 0) or (tahunkabisat2 is not 0): 
    print(f'Tahun {tahun} merupakan TAHUN KABISAT')


else : 
    print(f"Tahun {tahun} bukan Tahun kabisat")