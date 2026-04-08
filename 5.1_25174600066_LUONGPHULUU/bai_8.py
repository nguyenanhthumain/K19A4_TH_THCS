lst = []
print("Nhập các số nguyên (0 để dừng):")
while True:
    n = int(input())
    if n == 0:
        break
    lst.append(n)

print("Danh sách ban đầu:", lst)

# a:
x = int(input("Nhập x cần tìm: "))
found = False
for i in range(len(lst)):
    if lst[i] == x:
        print("Tìm thấy x tại vị trí:", i)
        pos = i
        found = True
        break
if not found:
    print("Không tìm thấy x")

# b:
if found:
    new_value = int(input("Nhập giá trị mới: "))
    lst[pos] = new_value
    print("Danh sách sau khi sửa:", lst)

# c:
y = int(input("Nhập y cần thêm: "))
print("1. Thêm đầu")
print("2. Thêm cuối")
print("3. Thêm giữa")
chon = int(input("Chọn: "))
if chon == 1:
    lst = [y] + lst
elif chon == 2:
    lst = lst + [y]
elif chon == 3:
    mid = len(lst) // 2
    lst = lst[:mid] + [y] + lst[mid:]
print("Danh sách sau khi thêm:", lst)

# d:
print("Danh sách trước khi sắp xếp:", lst)
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            # đổi chỗ
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print("Danh sách sau khi sắp xếp giảm dần:", lst)

# e:
print("Danh sách trước khi xóa:", lst)
k = int(input("Nhập vị trí cần xóa: "))
if 0 <= k < len(lst):
    lst = lst[:k] + lst[k+1:]
    print("Danh sách sau khi xóa:", lst)
else:
    print("Vị trí không hợp lệ")