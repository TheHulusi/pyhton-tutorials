fruits = ["apple", "banana", "cherry", "kivi", "mango"]
newlist = []
new99list = []


for x in fruits:
    if "a" in x:
        newlist.append(x)
    else:
        new99list.append(x)

print(newlist)
print(new99list)

i = 0
ikilist = []
uclist = []
dortlist = []
beslist = []
altılist = []

while i <= 100:
    if i % 2 == 0:
        ikilist.append(i)

    if i % 3 == 0:
        uclist.append(i)

    if i % 4 == 0:
        dortlist.append(i)

    if i % 5 == 0:
        beslist.append(i)

    if i % 6 == 0:
        altılist.append(i)

    i += 1

print(ikilist)
print(uclist)
print(dortlist)
print(beslist)
print(altılist)





i = 1
toplam = 0
while i < 100:
    if i % 2 == 1:
        toplam = toplam + i
    i +=1

print(toplam)





sayilar = []
for x in range(5):
    sayi = int(input())
    sayilar.append(sayi)
print(sayilar)