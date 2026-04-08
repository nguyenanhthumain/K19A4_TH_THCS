a = []
while True:
    x = int(input("Nhập số (0 dừng): "))
    if x==0:
        break
    a.append(x)

#a dương lên đầu
duong = []
am = []
for x in a:
    if x>0:
        duong.append(x)
    else:
        am.append(x)
a = duong + am
print("Dương lên đầu:", a)

#b chèn số m
m = int(input("Nhập số m: "))
a.insert(0,m)
a.append(m)
if len(a)>=5:
    a.insert(4,m)
else:
    a.append(m)
print("Sau khi chèn m:", a)