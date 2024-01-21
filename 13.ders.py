def myfunction (name,surname):
    print("Hoşgeldin ",name , surname)

isim = input("İsmini gir lan:")
soyisim = input("soyismini gir lan:")
myfunction(isim,soyisim)






def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("zaha", "okan buruk", "arda güler")






def listeyeekle(*sayi):
    sayilar = []
    sayilar.append(sayi)
    print(sayilar)

listeyeekle(23,34,45,67,89,23,45,67,89)





def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")






def myfunction (name,surname):
    print("Hoşgeldin ",name , surname)



isim = input("İsmini gir lan:")
soyisim = input("soyismini gir lan:")
myfunction(name=isim,surname=soyisim)







def my_function(**kid):
  print("onun soyadı " + kid["lname"])

my_function(fname = "okan", lname = "buruk")






def my_function(**kid):
  print("çocuğun bilgileri " , kid)

my_function(isim = "okan", soyisim = "buruk" , yas = 99)







def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")









def myfunction(name,phonenumber = "telefon girilmedi"):
  print(name,"ın telefon numarası",phonenumber,"budur")
myfunction("icardi")
myfunction("icardi","0 000 000 00 00")