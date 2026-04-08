a = []
while True:
    val = int(input("Nhập số (nhập 0 để dừng): "))
    if val == 0: break
    a.append(val)

# a. Chèn danh sách [1,2,3]
add = [1, 2, 3]
a = add + a               # Vị trí đầu
a = a + add               # Vị trí cuối
if len(a) >= 5:
    a[4:4] = add          # Chèn vào vị trí thứ 5 (index 4)
print("4a. Sau khi chèn [1,2,3]:", a)

# b. Xóa phần tử thứ k
k = int(input("Nhập vị trí k cần xóa (bắt đầu từ 1): "))
if 1 <= k <= len(a):
    a.pop(k-1)
print(f"4b. Sau khi xóa phần tử thứ {k}:", a)

# c. Sắp xếp (Thuật toán Bubble Sort - không dùng hàm có sẵn)
n = len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("4c. Tăng dần:", a)
print("4c. Giảm dần:", a[::-1])