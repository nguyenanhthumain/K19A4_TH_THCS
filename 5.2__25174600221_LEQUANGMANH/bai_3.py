a = []
while True:
    val = int(input("Nhập số (nhập 0 để dừng): "))
    if val == 0: break
    a.append(val)

# a. Chuyển số dương lên đầu
duong = [x for x in a if x > 0]
con_lai = [x for x in a if x <= 0]
a = duong + con_lai
print("3a. Danh sách sau khi chuyển số dương lên đầu:", a)

# b. Chèn số m
m = int(input("Nhập số m cần chèn: "))
a.insert(0, m)            # Đầu
a.append(m)               # Cuối
if len(a) >= 5:
    a.insert(4, m)        # Vị trí thứ 5 (index 4)
print("3b. Danh sách sau khi chèn m:", a)