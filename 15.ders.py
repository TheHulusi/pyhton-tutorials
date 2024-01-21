






def pizzalma():
    KUCUK_BOY_FIYAT = 149.99
    ORTA_BOY_FIYAT = 189.99
    BUYUK_BOY_FIYAT = 249.99
    KUCUK_BOY_PEYNIR_FIYAT = 10
    DIGER_BOY_PEYNIR_FIYAT = 19.90
    ICECEK_FIYAT = 39.99

    print(" ----MENÜ----")
    print("KÜÇÜK BOY PİZZA: 149.99")
    print("ORTA BOY PİZZA: 189.99")
    print("BÜYÜK BOY PİZZA: 249.99")
    print("İÇECEK: 39.99")
    print("EKSTRA PEYNİR: 19.90")
    print("---------------")
    print("Hulusi Pizza'ya hoşgeldiniz...")

    boyut = input('Hangi boy pizza istiyorsunuz? küçük, orta veya büyük').upper()
    ekstra_peynir = input('Fazladan peynir istiyor musunuz? ').lower()
    icecek = input('Yanına içecek istiyor musunuz?').lower()

    hesap = 0

    if boyut == "küçük":
        hesap += KUCUK_BOY_FIYAT
    elif boyut == "orta":
        hesap += ORTA_BOY_FIYAT
    else:
        hesap += BUYUK_BOY_FIYAT

    if ekstra_peynir == "evet":
        if boyut == "S":
            hesap += KUCUK_BOY_PEYNIR_FIYAT
        else:
            hesap += DIGER_BOY_PEYNIR_FIYAT

    if icecek == "evet":
        hesap += ICECEK_FIYAT

    print(f"Toplam tutarı: {hesap} Kuruş.")


pizzalma()









sayi = int(input("lütfen kenar uzunluğunu giriniz: "))
for i in range(sayi):
    print("")
    for j in range(sayi):
        if i == 0 or j == 0 or i == sayi - 1 or j == sayi - 1:
            print("*",end=" ")
        else:
            print(" ", end=" ")