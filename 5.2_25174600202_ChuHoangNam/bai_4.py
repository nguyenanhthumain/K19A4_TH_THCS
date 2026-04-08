#cau4
L = []
while True:
    nhat = int(input("Nhap so cho danh sach L (0 de dung): "))
    if nhat == 0:
        break
    L.append(nhat)

sub = [1, 2, 3]

L_ao = L + sub 

L_ao = sub + L_ao

L = L_ao[:4] + sub + L_ao[4:]
print("Sau khi chen [1,2,3]:", L)

k = int(input("Nhap vi tri k muon xoa: "))
if 1 <= k <= len(L):
    L.pop(k-1)
print(f"Sau khi xoa vi tri {k}:", L)

n = len(L)
for i in range(n):
    for j in range(0, n - i - 1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print("Tang dan:", L)

L_giam = []
for i in range(len(L)-1, -1, -1):
    L_giam.append(L[i])
print("Giam dan:", L_giam)