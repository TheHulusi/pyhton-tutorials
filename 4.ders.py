print("notunuzu giriniz")
sayi1 = int(input())
sayi2 = int(input())
ortalama = (sayi1 + sayi2) / 2
print("ortalama")
if sayi1 >= 0 and sayi1 <= 100 and sayi2 >= 0 and sayi2 <= 100:
    if ortalama <= 100 and ortalama >= 85:
        print("AA")

    if 100 >= ortalama and ortalama >= 85:
        print("AB")
    elif ortalama >= 80:
        print("BB")
    elif ortalama >= 70:
        print("BC")
    elif ortalama >= 65:
        print("CC")
    elif ortalama >= 60:
        print("CD")
    elif ortalama >= 55:
        print("DD")
    elif ortalama >= 50:
        print("")

else:
    print("FF")





print("bir sayı giriniz")
a = int(input())
if a % 2 == 0:
    print ("sayı çiftir")
else:
    print("sayı tektir")




sifre = "icardi1905"
print ("lütfen şifreni gir kanks.")
parola = (str(input()))
if sifre == parola:
    print("basarıyla giriş yaptın kanki")
else:
    print("giriş yapamadın kanks")
    print("şifreni değiştircenmi kanks")

    if cevap = "evet"
        print ("yeni şifreni gir kanks")
        cevap = (str(input()))
        print ("yeni şifren oluşturuldu gule gule kullan")
    else:
        print ("cabuk burdan kaybol")