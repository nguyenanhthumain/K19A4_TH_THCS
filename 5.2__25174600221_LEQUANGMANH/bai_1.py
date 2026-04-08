# Nhập số lượng phần tử n
n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(val)

print("Danh sách vừa nhập:", a)

# a. Tổng các phần tử
tong = 0
for x in a:
    tong += x
print(f"a. Tổng các phần tử: {tong}")

# b. Đếm số dương và tổng số dương
count_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        count_duong += 1
        tong_duong += x
print(f"b. Số lượng số dương: {count_duong}, Tổng số dương: {tong_duong}")

# c. Vị trí phần tử âm đầu tiên
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
print(f"c. Vị trí phần tử âm đầu tiên: {vi_tri_am_dau}")

# d. Vị trí phần tử dương cuối cùng
vi_tri_duong_cuoi = -1
for i in range(len(a) - 1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
print(f"d. Vị trí phần tử dương cuối cùng: {vi_tri_duong_cuoi}")

# e. Phần tử lớn nhất và vị trí cuối cùng
if len(a) > 0:
    max_val = a[0]
    vi_tri_max_cuoi = 0
    for i in range(len(a)):
        if a[i] >= max_val: # Dùng >= để lấy vị trí cuối cùng
            max_val = a[i]
            vi_tri_max_cuoi = i
    print(f"e. Phần tử lớn nhất: {max_val}, Vị trí cuối cùng: {vi_tri_max_cuoi}")