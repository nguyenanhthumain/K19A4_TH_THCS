#cau8
L = []
while True:
    so = int(input("Nhap so nguyen (nhap 0 để dung): "))
    if so == 0:
        break
    L.append(so)
x = int(input("\nNhap gia tri x can tim de sua: "))
tim_thay = False
for i in range(len(L)):
    if L[i] == x:
        print(f"Tim thay {x} tai vi tri (index): {i}")
        gia_tri_moi = int(input("Nhap gia tri moi de thay the: "))
        L[i] = gia_tri_moi
        tim_thay = True
        break 
if not tim_thay:
    print("Khong tim thay x trong danh sach")
print("Danh sach sau khi sua:", L)

y = int(input("\nNhap gia tri y muon them: "))

L.insert(0, y)

L.append(y)

vi_tri_giua = len(L) // 2
L.insert(vi_tri_giua, y)
print("Danh sach sau khi y vao dau ,cuoi va giua:", L)

print("\nDanh sach truoc khi sap xep:", L)
n_list = len(L)
for i in range(n_list):
    for j in range(0, n_list - i - 1):
        if L[j] < L[j + 1]: 
            tam = L[j]
            L[j] = L[j + 1]
            L[j + 1] = tam
print("Danh sách sau khi sap xep giam dan:", L)
vi_tri_xoa = int(input("\nNhap vi tri (index) muon xoa: "))
if 0 <= vi_tri_xoa < len(L):
    print("Danh sach truoc khi xoa:", L)
    L.pop(vi_tri_xoa)
    print("Danh sach sau khi xoa:", L)
else:
    print("Vi tri không hop le.")