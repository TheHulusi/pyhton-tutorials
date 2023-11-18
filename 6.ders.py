list = [1,2,2,3,4,5,6,7,7,8,9,0]
for i in list:
    if list[i] == list[i+1]:
       print(list[i])



for x in range(6):
    if x == 3: pass
    print(x)
else:
    print("finally finished")

    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    adet = [1, 2, 3]
    for x in adj:
        for y in fruits:
            for z in adet:
                print(x, y, z)





list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]

for i in list1:
    print("--------------")
    for x in list2:
        if x == i:
            print(i*x)