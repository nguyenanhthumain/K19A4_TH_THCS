lst = []
print("Nhập các số nguyên:")
while True:
    num = int(input())
    if num == 0:
        break
    lst.append(num)

print("Danh sách ban đầu:", lst)

#a.
x = int(input("\nNhập giá trị x cần tìm: "))

if x in lst:
    pos = lst.index(x)
    print(f"Phần tử {x} được tìm thấy tại vị trí:", pos)
else:
    print(f"Không tìm thấy {x} trong danh sách.")

#b.
if x in lst:
    new_value = int(input("Nhập giá trị mới để thay cho x: "))
    lst[pos] = new_value
    print("Danh sách sau khi chỉnh sửa:", lst)

#c.
y = int(input("\nNhập giá trị y cần thêm: "))
print("1. Thêm vào đầu")
print("2. Thêm vào giữa")
print("3. Thêm vào cuối")

choice = int(input("Chọn vị trí thêm (1/2/3): "))

if choice == 1:
    lst.insert(0, y)
elif choice == 2:
    mid = len(lst) // 2
    lst.insert(mid, y)
elif choice == 3:
    lst.append(y)
else:
    print("Lựa chọn không hợp lệ!")

print("Danh sách sau khi thêm y:", lst)

#d.
print("\nDanh sách trước khi sắp xếp:", lst)
for i in range(len(lst)):
    max_idx = i
    for j in range(i + 1, len(lst)):
        if lst[j] > lst[max_idx]:
            max_idx = j
    lst[i], lst[max_idx] = lst[max_idx], lst[i]

print("Danh sách sau khi sắp xếp giảm dần:", lst)

#e.
print("\nDanh sách hiện tại:", lst)
delete_value = int(input("Nhập giá trị cần xóa: "))

if delete_value in lst:
    lst.remove(delete_value)
    print("Danh sách sau khi xóa:", lst)
else:
    print("Không tìm thấy giá trị cần xóa.")