a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)
print("Danh sách ban đầu:", a)

# a.
insert_list = [1, 2, 3]
a = insert_list + a
a = a + insert_list
if len(a) >= 5:
    a = a[:4] + insert_list + a[4:]
else:
    a = a + insert_list
print("a. Danh sách sau khi chèn:", a)

# b.
k = int(input("Nhập vị trí k cần xóa: "))
if 1 <= k <= len(a):
    del a[k - 1]
else:
    print("Vị trí k không hợp lệ")

print("b. Danh sách sau khi xóa k:", a)

# c.
tang = sorted(a)
giam = sorted(a, reverse=True)
print("c. Tăng dần:", tang)
print("   Giảm dần:", giam)