print("""**********
Hesap Makinesi Programi

1.Toplama

2.Cikarma

3.Carpma

4.Bolme
**********

""")

sayi1 = int(input("ilk sayiyi giriniz: "))
sayi2 = int(input("ikinci sayiyi giriniz: "))

islem = input("islemi giriniz: ")

if(islem == '1'):
    print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))
elif(islem == '2'):
    print("{} - {} = {}".format(sayi1,sayi2,sayi1-sayi2))
elif(islem == '3'):
    print("{} * {} = {}".format(sayi1,sayi2,sayi1*sayi2))
elif(islem == '4'):
    print("{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2))
else:
    print("Gecersiz islem")
    










