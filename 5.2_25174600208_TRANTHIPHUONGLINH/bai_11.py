import random

n = int(input("Nhập số phần tử A: "))
A = []
for i in range(n):
    A.append(int(input("Nhập phần tử thứ {}: ".format(i))))
# tạo danh sách
D = []
for i in range(len(A)):
    if A[i] % 3 == 0:
        D.append(A[i])

if len(D) > 0:
    vt = random.randint(0, len(D)-1)
    print("Ngẫu nhiên từ D:", D[vt])
else:
    print("Không có số chia hết 3")