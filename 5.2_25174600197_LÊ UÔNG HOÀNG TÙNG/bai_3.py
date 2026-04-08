#bai3
a = []
print("nhap cac so, nhap 0 de ket thuc:")
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)
print("danh sach ban dau:", a)
duong = [x for x in a if x > 0]
am = [x for x in a if x <= 0]
a_moi = duong + am
print("danh sach sau khi chuyen duong len dau:", a_moi)
m = int(input("nhap so m can chen: "))
a_moi.insert(0, m)                    
a_moi.append(m)                       
if len(a_moi) >= 5:
    a_moi.insert(5, m)                
print("danh sach sau khi chen m:", a_moi)