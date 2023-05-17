def faktoryel(sayi):
    fak=1
    for i in range(1,sayi+1):
        fak*=i
    return fak
sayi=int(input("bir sayi giriniz:"))
print(f"{sayi}!:",faktoryel(sayi))
