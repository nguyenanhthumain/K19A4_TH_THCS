a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)
print("Danh sách ban đầu:", a)
# a:
duong = []
khac = []
i = 0
while i < len(a):
    if a[i] > 0:
        duong.append(a[i])
    else:
        khac.append(a[i])
    i += 1
a = duong + khac
print("Danh sách sau khi đưa số dương lên đầu:", a)
# b:
m = int(input("Nhập m: "))
a.insert(0, m)
a.append(m)
if len(a) >= 4:
    a.insert(4, m)
else:
    a.append(m)
print("Danh sách sau khi chèn:", a)