lst = []
print("Nhập các số (nhập 0 để kết thúc):")
while True:
    x = int(input())
    if x == 0:
        break
    lst.append(x)
print("Danh sách ban đầu:", lst)
# a:
insert_list = [1, 2, 3]

lst_dau = insert_list + lst
print("Chèn vào đầu:", lst_dau)

lst_cuoi = lst + insert_list
print("Chèn vào cuối:", lst_cuoi)

if len(lst) >= 4:
    lst_giua = lst[:4] + insert_list + lst[4:]
else:
    lst_giua = lst + insert_list
print("Chèn vào vị trí thứ 5:", lst_giua)

# b:
k = int(input("Nhập k (vị trí cần xóa, bắt đầu từ 1): "))
if 1 <= k <= len(lst):
    lst_xoa = lst[:k-1] + lst[k:]
    print("Danh sách sau khi xóa:", lst_xoa)
else:
    print("k không hợp lệ!")

# c:
lst_tang = lst[:]
n = len(lst_tang)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst_tang[j] > lst_tang[j + 1]:
            temp = lst_tang[j]
            lst_tang[j] = lst_tang[j + 1]
            lst_tang[j + 1] = temp
print("Danh sách tăng dần:", lst_tang)

lst_giam = lst[:]
n = len(lst_giam)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst_giam[j] < lst_giam[j + 1]:
            temp = lst_giam[j]
            lst_giam[j] = lst_giam[j + 1]
            lst_giam[j + 1] = temp
print("Danh sách giảm dần:", lst_giam)