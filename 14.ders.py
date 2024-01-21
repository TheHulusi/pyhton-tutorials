def Faktoriyel():
  n = int(input("faktoriyelini hesaplamak istediğiniz sayıyı giriniz"))
  i = 1
  carpim = 1

  while i <=n:
    carpim = carpim*i
    i += 1
  print(n,"sayısının faktoriyeli = ",carpim)



Faktoriyel()










n=int(input("kontrol etmek istediğiniz sayıyı giriniz"))
i=2
while i< n:
    if n % i==0:
        print("bu sayı asal değildir")
        break
    i+=1
else:
    print("bu sayı asaldır")












def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))