#bai_2
"""
2. Viết chương trình nhập vào một danh sách các phần tử là số tự nhiên với số phần
tử bằng n (n nhập từ bàn phím). Thực hiện các yêu cầu sau.
a. Tìm phần tử và vị trí của phần tử có giá trị lớn thứ hai của danh sách.
b. Tính số lượng các số dương liên tiếp nhiều nhất.
c. Tính số lượng các số dương liên tiếp có tổng lớn nhất.
"""

n = int(input("Nhập số phần tử của danh sách: "))
ds = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    ds.append(phan_tu)

#a
max1 = max(ds)
for i in ds :
    if i < max1:
        max2 = i
    elif i > max2 and i < max1:
        max2 = i
if max1 != -1 :
    print(f"Phần tử có giá trị lớn thứ hai của danh sách: {max2}")