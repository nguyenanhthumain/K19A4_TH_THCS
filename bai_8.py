lst = []

while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    lst.append(x)
x = int(input("Tìm x: "))
if x in lst:
    print("Vị trí:", lst.index(x))
else:
    print("Không có")
if x in lst:
    new = int(input("Giá trị mới: "))
    lst[lst.index(x)] = new
print(lst)
y = int(input("Nhập y: "))
pos = int(input("Vị trí (0-đầu): "))
lst.insert(pos, y)
print(lst)
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)
del_index = int(input("Xóa vị trí: "))
if 0 <= del_index < len(lst):
    lst.pop(del_index)
print(lst)