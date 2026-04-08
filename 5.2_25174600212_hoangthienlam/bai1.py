
try:
    n = int(input("Nhập độ dài n của danh sách: "))
    a = []
    for i in range(n):
        val = int(input(f"Nhập phần tử thứ {i}: "))
        a.append(val)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ!")
    a = []
if len(a) > 0:
    tong_tat_ca = 0
    for x in a:
        tong_tat_ca += x
    print(f"a. Tổng các phần tử: {tong_tat_ca}")
    dem_duong = 0
    tong_duong = 0
    for x in a:
        if x > 0:
            dem_duong += 1
            tong_duong += x
    print(f"b. Số lượng số dương: {dem_duong}, Tổng số dương: {tong_duong}")
    vi_tri_am_dau = -1
    for i in range(len(a)):
        if a[i] < 0:
            vi_tri_am_dau = i
            break
    if vi_tri_am_dau != -1:
        print(f"c. Vị trí phần tử âm đầu tiên: {vi_tri_am_dau}")
    else:
        print("c. Không có số âm trong danh sách.")
    vi_tri_duong_cuoi = -1
    for i in range(len(a) - 1, -1, -1):
        if a[i] > 0:
            vi_tri_duong_cuoi = i
            break
    if vi_tri_duong_cuoi != -1:
        print(f"d. Vị trí phần tử dương cuối cùng: {vi_tri_duong_cuoi}")
    else:
        print("d. Không có số dương trong danh sách.")
    max_val = a[0]
    vi_tri_max_cuoi = 0
    for i in range(len(a)):
        if a[i] >= max_val: 
            max_val = a[i]
            vi_tri_max_cuoi = i
    print(f"e. Phần tử lớn nhất: {max_val}, Vị trí cuối cùng của nó: {vi_tri_max_cuoi}")