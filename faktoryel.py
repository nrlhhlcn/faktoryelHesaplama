def faktoryel(sayi1,sayi2): # faktoryel hesaplayan fonksiyon
    fak1=1
    fak2=1
    if sayi1<1 or sayi2<1:
        print("hatalı veri girişi")
    else:
        for i in range(1,sayi1+1):
            fak1*=i
        for i in range(1,sayi2+1):
            fak2*=i



        print(f"{sayi1}!-{sayi2}!:",fak1-fak2)
sayi1=int(input("birinci sayi giriniz:"))
sayi2=int(input("ikinci sayi giriniz:"))
faktoryel(sayi1,sayi2)
