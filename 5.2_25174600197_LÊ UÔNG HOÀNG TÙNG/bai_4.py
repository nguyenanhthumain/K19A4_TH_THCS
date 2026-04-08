#bai4
a = []
print("nhap cac so, nhap 0 de ket thuc:")
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)
print("danh sach ban dau:", a)
a.insert(0, [1,2,3])                 
a.append([1,2,3])                     
if len(a) >= 5:
    a.insert(5, [1,2,3])              
print("sau khi chen [1,2,3]:", a)
k = int(input("nhap vi tri k can xoa (bat dau tu 0): "))
if 0 <= k < len(a):
    del a[k]
    print("sau khi xoa vi tri", k, ":", a)
else:
    print("vi tri khong hop le")
tang = sorted(a)
giam = sorted(a, reverse=True)
print("sap xep tang dan:", tang)
print("sap xep giam dan:", giam)