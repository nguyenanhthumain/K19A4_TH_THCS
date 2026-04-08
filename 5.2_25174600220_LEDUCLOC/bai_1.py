"""1. Cho danh sách a có độ dài là n với các phần tử là số tự nhiên chứa cả giá trị âm và
dương được nhập từ bàn phím. Yêu cầu:
a. Viết chương trình tính tổng các phần tử của danh sách.
b. Viết chương trình đếm số lượng các số hạng dương và tổng của các số hạng
dương.
c. Tìm vị trí của phần tử âm đầu tiên trong danh sách.
d. Tìm vị trí của phần tử dương cuối cùng trong danh sách."""


# a
a = list(map(int, input("Nhập danh sách a (các phần tử cách nhau bằng dấu cách): ").split()))
tong = sum(a)
print(f"Tổng các phần tử của danh sách là: {tong}")

# b
dem = 0
tong_duong = 0
for i in a:
    if i > 0:
        dem += 1
        tong_duong += i
print(f"Số lượng các số dương của danh sách là: {dem}")
print(f"Tổng các số dương của danh sách là: {tong_duong}")

# c. Tìm vị trí của phần tử âm đầu tiên trong danh sách a
for i in range(len(a)):
    if a[i] < 0:
        print(f"Vị trí của phần tử âm đầu tiên trong danh sách là: {i}")
        break    

# d. Tìm vị trí của phần tử dương cuối cùng trong danh sách a
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        print(f"Vị trí của phần tử dương cuối cùng trong danh sách là: {i}")
        break