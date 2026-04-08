"""11. Viêt chương trình tạo một danh sách A có n phần tử là số nguyên được nhập từ
bàn phím. Sử dụng List Comprehension thực hiện các yêu cầu sau:

a. Tạo ra một danh sách B chứa các phần tử chia hết cho 3 nhưng không chia
hết cho 5 từ danh sách ban đầu. In kết quả ra màn hình.
b. Tạo một danh sách C với các phần tử là bình phương của danh sách A.
c. Tạo ra danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia
hết cho 3."""

n = int(input("Nhập số phần tử của danh sách A: "))
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    a.append(x)
#a
b = [x for x in a if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", b)
#b
c = [x**2 for x in a]
print("Danh sách C:", c)
#c
d = [x for x in a if x % 3 == 0]
print("Danh sách D:", d)