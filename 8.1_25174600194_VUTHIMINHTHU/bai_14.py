n = int(input("Nhập số lượng phần tử n: "))
danh_sach = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(so)
print(f"\nDanh sách ban đầu: {danh_sach}")
list_binh_phuong = list(map(lambda x: x**2, danh_sach))
print(f"Danh sách bình phương: {list_binh_phuong}")
