import math

def faktoriyel():
    sayi = int(input("lütfen faktoriyelini almak istadiğiniz sayıyı gireiniz"))
    print(math.factorial(sayi))

faktoriyel()







import random
import time


while True:
    sayi = random.randint(1, 100)
    tahmin=int(input("tahmınınızı gırınız:  "))
    if sayi == tahmin:
        print("oyunu kazandınız")
    else:
        print("oyunu kaybettiniz",sayi)

    if sayi>tahmin:
        print("daha yuksek bır sayı gırınız")
    else:
        sayi<tahmin
        print("daha dusuk bır sayı gırınız")







import time
import random
while True:
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")


    randomsayi=random.randint(1,3)

    if randomsayi == 1:
        print("taş")
    elif randomsayi == 2:
        print("kağıt")
    else:
        print("makas")