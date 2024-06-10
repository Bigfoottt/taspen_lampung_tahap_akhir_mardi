def cetak_gambar(panjang):
    
    if panjang % 2 == 0:
        print("Panjang harus merupakan bilangan ganjil.")
        return
    
    for i in range(panjang):
        for j in range(panjang):
            if j == 0 or j == panjang - 1 or i == panjang // 2:
                print("*", end=" ")
            else:
                print("=", end=" ")
        print()
        
cetak_gambar(5)