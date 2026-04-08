danh_sach = []
print("Nhập thông tin (name, age, score). Để trống và nhấn Enter để dừng.")
while True:
    s = input("Nhập (vd: Tom,19,80): ")
    if not s:
        break
    parts = s.split(",")
    danh_sach.append((parts[0].strip(), int(parts[1].strip()), int(parts[2].strip())))
danh_sach.sort(key=lambda x: (x[0], x[1], x[2]))
print("\nDanh sách sau khi sắp xếp:")
print(danh_sach)