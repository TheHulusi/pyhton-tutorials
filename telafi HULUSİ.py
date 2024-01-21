for i in range(0,1000,7):

    if i == 0:
        continue
    print(i)





for i in range(5,100,3):
    print(i+1)

for i in range(58,220,9):
    print(i+5)
ikiilebolunenler=[]
ucilebolunenler=[]
yediilebolunenler=[]
besilebolunenler=[]
for i in range(101):
    if i%2==0:
        ikiilebolunenler.append(i)
    if i%3==0:
        ucilebolunenler.append(i)
    if i%5==0:
        besilebolunenler.append(i)
    if i%7==0:
        yediilebolunenler.append(i)

print(ikiilebolunenler)
print(ucilebolunenler)
print(yediilebolunenler)
print(besilebolunenler)

