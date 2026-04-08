n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(val)

# a. Tìm phần tử và vị trí của phần tử lớn thứ hai
# Bước 1: Tìm Max lớn nhất
max1 = a[0]
for x in a:
    if x > max1:
        max1 = x

# Bước 2: Tìm Max lớn thứ hai (max2 < max1)
max2 = None
for x in a:
    if x < max1:
        if max2 is None or x > max2:
            max2 = x

if max2 is None:
    print("a. Không có số lớn thứ hai.")
else:
    vi_tri_max2 = []
    for i in range(len(a)):
        if a[i] == max2:
            vi_tri_max2.append(i)
    print(f"a. Giá trị lớn thứ hai: {max2}, Vị trí: {vi_tri_max2}")

# b. Số lượng các số dương liên tiếp nhiều nhất
max_lien_tiep = 0
current_count = 0
for x in a:
    if x > 0:
        current_count += 1
        if current_count > max_lien_tiep:
            max_lien_tiep = current_count
    else:
        current_count = 0
print(f"b. Số lượng số dương liên tiếp nhiều nhất: {max_lien_tiep}")

# c. Số lượng các số dương liên tiếp có tổng lớn nhất
max_sum = 0
current_sum = 0
current_len = 0
best_len = 0

for x in a:
    if x > 0:
        current_sum += x
        current_len += 1
        if current_sum > max_sum:
            max_sum = current_sum
            best_len = current_len
    else:
        current_sum = 0
        current_len = 0
print(f"c. Số lượng phần tử của dãy dương có tổng lớn nhất: {best_len} (Tổng = {max_sum})")