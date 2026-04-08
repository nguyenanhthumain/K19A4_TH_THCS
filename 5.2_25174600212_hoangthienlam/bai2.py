n = int(input("Nhập n: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i}: ")))
if len(a) < 2:
    print("Danh sách cần ít nhất 2 phần tử để tìm số lớn thứ hai.")
else:
    m1 = a[0]
    for x in a:
        if x > m1: m1 = x
    m2 = -float('inf')
    vi_tri_m2 = -1
    for i in range(len(a)):
        if a[i] < m1 and a[i] > m2:
            m2 = a[i]
            vi_tri_m2 = i 
    if vi_tri_m2 != -1:
        print(f"Phần tử lớn thứ hai là {m2} tại vị trí {vi_tri_m2}")
    else:
        print("Không có số lớn thứ hai (các số bằng nhau).")
max_count = 0
current_count = 0
max_sum = 0
current_sum = 0
for x in a:
    if x > 0:
        current_count += 1
        current_sum += x
    else:
        if current_count > max_count: max_count = current_count
        if current_sum > max_sum: max_sum = current_sum
        current_count = 0
        current_sum = 0
if current_count > max_count: max_count = current_count
if current_sum > max_sum: max_sum = current_sum
print(f"Số lượng số dương liên tiếp nhiều nhất: {max_count}")
print(f"Tổng số dương liên tiếp lớn nhất: {max_sum}")