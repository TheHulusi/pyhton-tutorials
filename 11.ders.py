i = 0
while i <= 12:
    print(i,". sınıf")
    i += 1




i = 1
while True:
    print(i, ". sınıf")
    i += 1
    if i == 13:
        break








while True:
    print("8 Karakterli şifrenzi giriniz")
    sifre = str(input())
    karakters = 0
    for x in sifre:
        karakters += 1
    if karakters < 8 or karakters > 8:
        print("Şifreniz 8 haneli olmalıdır"),
    else:
        print("Şifreniz kaydedilmiştir")
        print("çıkış yapmak istiyorsanız (Çıkış yap) yazınız.")
        x = str(input())
    if x == "Çıkış yap":
            break




while True:
    i = input("lütfen kelıme secımını yapınız")
    print(i.upper())







while True:
    i = int(input("lütfen bir sayı giriniz"))
    x = 1
    carpanlar = []
    while x <= i:
        if i % x == 0:
            carpanlar.append(x)
        x += 1
    print(carpanlar)
