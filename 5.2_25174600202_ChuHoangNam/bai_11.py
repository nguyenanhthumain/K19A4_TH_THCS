#cau11
n = int(input("Nhap so luong phan tu n: "))
A = []

for i in range(n):
    tmp = int(input(f"Nhap phan tu thu {i+1}: "))
    A.append(tmp)

print("\nDanh sach A ban dau:", A)

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("a. Danh sach B (chia het cho 3, khong cho 5):", B)

C = [x**2 for x in A]
print("b. Danh sach C (binh phuong cua A):", C)

danh_sach_chia_het_3 = [x for x in A if x % 3 == 0]

if len(danh_sach_chia_het_3) > 0:
    chi_so_ngau_nhien = id(danh_sach_chia_het_3) % len(danh_sach_chia_het_3)
    D = [danh_sach_chia_het_3[chi_so_ngau_nhien]]
else:
    D = [] 

print("c. Danh sach D (ngau nhien tu A chia het cho 3):", D)