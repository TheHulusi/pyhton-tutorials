i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1








i = 1
toplam = 1

while i < 20:
  i += 1
  toplam += i
  if toplam >= 102:
      print(i,"sayısı ile 102 yi geçmiştir")
      print(toplam)
      break

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)





i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")