import random

n = int(input("Nhập số lượng phần tử n: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)
C = [x**2 for x in A]
print("Danh sách C:", C)
chia_het_3 = [x for x in A if x % 3 == 0]
if chia_het_3:
    D = [random.choice(chia_het_3) for _ in range(min(2, len(chia_het_3)))]
    print("Danh sách D (ngẫu nhiên):", D)
else:
    print("Danh sách D trống vì không có số nào chia hết cho 3")