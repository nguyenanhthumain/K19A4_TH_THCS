#bai8
danhsach = []
print("nhap cac so nguyen, nhap 0 de ket thuc:")
while True:
    x = int(input())
    if x == 0:
        break
    danhsach.append(x)
print("danh sach ban dau:", danhsach)
x = int(input("nhap gia tri x can tim: "))
if x in danhsach:
    vitri = danhsach.index(x)
    print("tim thay", x, "tai vi tri thu", vitri)
else:
    print("khong tim thay", x, "trong danh sach")
if x in danhsach:
    giatri_moi = int(input("nhap gia tri moi thay the cho " + str(x) + ": "))
    danhsach[vitri] = giatri_moi
    print("danh sach sau khi chinh sua:", danhsach)
y = int(input("nhap gia tri y can them: "))
vitri_them = input("them vao dau/cuoi/giua? (dau/cuoi/giua): ").lower()
if vitri_them == "dau":
    danhsach.insert(0, y)
elif vitri_them == "cuoi":
    danhsach.append(y)
elif vitri_them == "giua":
    giua = len(danhsach) // 2
    danhsach.insert(giua, y)
else:
    print("vi tri khong hop le, mac dinh them vao cuoi")
    danhsach.append(y)
print("danh sach sau khi them", y, ":", danhsach)
print("danh sach truoc khi sap xep:", danhsach)
for i in range(len(danhsach)):
    for j in range(i+1, len(danhsach)):
        if danhsach[i] < danhsach[j]:
            danhsach[i], danhsach[j] = danhsach[j], danhsach[i]
print("danh sach sau khi sap xep giam dan:", danhsach)
if danhsach:
    vitri_xoa = int(input("nhap vi tri can xoa (bat dau tu 0): "))
    if 0 <= vitri_xoa < len(danhsach):
        print("danh sach truoc khi xoa:", danhsach)
        del danhsach[vitri_xoa]
        print("danh sach sau khi xoa:", danhsach)
    else:
        print("vi tri xoa khong hop le")
else:
    print("danh sach rong, khong the xoa")