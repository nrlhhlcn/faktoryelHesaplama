def faktoryel(sayi): # faktoryel hesaplayan fonksiyon
    fak=1
    if sayi<1:
        print("hatalı veri girişi")
    else:
        for i in range(1,sayi+1):
            fak*=i
        print(f"{sayi}!:",fak)
sayi=int(input("bir sayi giriniz:"))
faktoryel(sayi)
