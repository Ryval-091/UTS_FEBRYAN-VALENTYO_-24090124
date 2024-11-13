jumlah_barang = int(input(f"masukkan jumlah barang     : "))
total = 0

for i in range(1, jumlah_barang +1 ):
    harga_barang = int(input(f'Masukkan harga Barang ke-{i} : '))

    total += harga_barang

int(print(f"total belanjaan             :Rp.{total}"))