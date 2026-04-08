"""4. Viết chương trình nhập vào một danh sách (list) các phần tử là số tự nhiên (có thể
nhận giá trị âm và dương) cho đến khi nhập vào số 0. Thực hiện các yêu cầu sau:
a. Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách.
b. Xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.
c. Sắp xếp danh sách theo thứ tự tăng dần, giảm dần."""

a = []
while True:
    x = int(input("Nhập phần tử: "))
    if x == 0:
        break
    a.append(x)

# a
a.insert(0, 1)
a.insert(len(a), 2)
a.insert(4, 3)
print(a)

# b
k = int(input("Nhập vị trí cần xóa: "))
del a[k]
print(a)

# c
a.sort()
print(a)
a.sort(reverse=True)
print(a)