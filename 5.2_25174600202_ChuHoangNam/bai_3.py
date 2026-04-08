#cau3
a = []
while True:
    so = int(input("Nhap so tu nhien (0 de dung): "))
    if so == 0:
        break
    a.append(so)
duong = []
con_lai = []
for x in a:
    if x > 0:
        duong.append(x)
    else:
        con_lai.append(x)
a_moi = duong + con_lai
print("Danh sach sau khi dua so duong len dau:", a_moi)

m = int(input("Nhap so m can chen: "))

a_moi.insert(0, m)

a_moi.append(m)
if len(a_moi) >= 5:
    a_moi.insert(4, m)
else:
    a_moi.append(m) 
print("Danh sach sau khi chen m:", a_moi)