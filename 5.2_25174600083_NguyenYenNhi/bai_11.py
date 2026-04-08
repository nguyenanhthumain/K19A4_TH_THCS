#bai_11
"""
Viêt chương trình tạo một danh sách A có n phần tử là số nguyên được nhập từ
bàn phím. Sử dụng List Comprehension thực hiện các yêu cầu sau:
a. Tạo ra một danh sách B chứa các phần tử chia hết cho 3 nhưng không chia
hết cho 5 từ danh sách ban đầu. In kết quả ra màn hình.
b. Tạo một danh sách C với các phần tử là bình phương của danh sách A.
c. Tạo ra danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia
hết cho 3.
"""

n = int(input("Nhập số phần tử của danh sách: "))
ds = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    ds.append(phan_tu)
#a
B = [i for i in ds if i % 3 == 0 and i % 5 != 0]
print(f"Danh sách B là: {B}")
#b
C = [i**2 for i in ds]
print(f"Danh sách C là: {C}")
#c
chia_het_cho_3 = [i for i in ds if i % 3 == 0]
if chia_het_cho_3:
    ngau_nhien = id(chia_het_cho_3) % len(chia_het_cho_3)
    D = [ngau_nhien]
    print(f"Danh sách D là: {D}")