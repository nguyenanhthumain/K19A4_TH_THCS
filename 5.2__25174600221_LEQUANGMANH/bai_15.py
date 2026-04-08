X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))

# Dùng List Comprehension lồng nhau để tạo mảng 2 chiều
mang_2_chieu = [[i * j for j in range(Y)] for i in range(X)]

print(mang_2_chieu)