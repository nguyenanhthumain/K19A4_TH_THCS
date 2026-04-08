lst = []

while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    lst.append(x)

# a
find_x = int(input("Tìm x: "))
if find_x in lst:
    print("Vị trí:", lst.index(find_x))
else:
    print("Không có")

# b
if find_x in lst:
    new_val = int(input("Giá trị mới: "))
    lst[lst.index(find_x)] = new_val
    print("Sau sửa:", lst)

# c
y = int(input("Thêm y: "))
pos = int(input("Vị trí: "))
lst.insert(pos, y)
print("Sau thêm:", lst)

# d (không sort)
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Giảm dần:", lst)

# e
del_index = int(input("Xóa vị trí: "))
if 0 <= del_index < len(lst):
    lst.pop(del_index)

print("Sau xóa:", lst)