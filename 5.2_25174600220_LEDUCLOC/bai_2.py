"""2. Viết chương trình nhập vào một danh sách các phần tử là số tự nhiên với số phần
tử bằng n (n nhập từ bàn phím). Thực hiện các yêu cầu sau.
a. Tìm phần tử và vị trí của phần tử có giá trị lớn thứ hai của danh sách.
b. Tính số lượng các số dương liên tiếp nhiều nhất.
c. Tính số lượng các số dương liên tiếp có tổng lớn nhất."""

n = int(input("Nhập số phần tử của danh sách a: "))
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

#a
for i in range(n):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        print(f"Phần tử lớn thứ của danh sách là: {a[i]}")
        print(f"Vị trí của phần tử lớn thứ hai của danh sách là: {i}")
        break

#b
dem = 1
max = 1 
for i in range(1, n):
    if a[i] > a[i-1]:
        dem += 1
        if dem > max:
            max = dem
    else:
        dem = 1
print(f"Số lượng các số dương liên tiếp nhiều nhất của danh sách là: {max}")

#c
dem = 1
max = 1 
for i in range(1, n):
    if a[i] > a[i-1]:
        dem += 1
        if dem > max:
            max = dem
    else:
        dem = 1
print(f"Số lượng các số dương liên tiếp có tổng lớn nhất của danh sách là: {max}")