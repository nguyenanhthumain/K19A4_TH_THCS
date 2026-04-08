a = list(map(int, input("Nhập các phần tử của danh sách: ").split(",")))
n = len(a)
if n == 0:
    print("Danh sách rỗng!")
else:
    print(f"\nDanh sách đã nhập: {a}")
    print(f"a. Tổng các phần tử:",sum(a))
    so_duong = [x for x in a if x > 0]
    print(f"b. Số lượng số dương: {len(so_duong)}, Tổng số dương: {sum(so_duong)}")
    phan_tu_am = -1 
    for i in range(n):
        if a[i] < 0:
            phan_tu_am = i
        break 
    print(f"c. Vị trí phần tử âm đầu tiên: {phan_tu_am}")
    phan_tu_duong = -1
    for i in range(n - 1, -1, -1):
        if a[i] > 0:
            phan_tu_duong = i
            break
    print(f"d. Vị trí phần tử dương cuối cùng: {phan_tu_duong}")
    GTLN = max(a)
    phan_tu_lon_cuoi = (i for i in range(n-1, -1, -1) if a[i] == GTLN)
    print(f"e. Phần tử lớn nhất: {GTLN}, Vị trí cuối cùng: {phan_tu_lon_cuoi}")
