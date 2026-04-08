n = int(input("Nhập số phần tử n: "))
# Nhập danh sách
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(x)
print("Danh sách:", a)
# a:
max1 = max2 = -1
pos = -1
for i in range(n):
    if a[i] > max1:
        max1 = a[i]
for i in range(n):
    if a[i] != max1 and a[i] > max2:
        max2 = a[i]
        pos = i
if max2 == -1:
    print("Không tồn tại số lớn thứ hai")
else:
    print("Số lớn thứ hai:", max2)
    print("Vị trí:", pos)
# b:
max_count = 0
count = 0
for i in range(n):
    if a[i] > 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print("Số lượng số dương liên tiếp nhiều nhất:", max_count)
# c:
max_sum = 0
current_sum = 0
count = 0
max_len = 0
for i in range(n):
    if a[i] > 0:
        current_sum += a[i]
        count += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_len = count
    else:
        current_sum = 0
        count = 0
print("Số lượng phần tử của đoạn dương có tổng lớn nhất:", max_len)