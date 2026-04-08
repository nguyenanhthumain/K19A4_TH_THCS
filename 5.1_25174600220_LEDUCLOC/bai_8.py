#Bài 8:
"""
Viết chương trình tạo một list với các giá trị là số nguyên nhập từ bàn phím, việc
nhập liệu kết thúc khi gõ phím “0”. Thực hiện các công việc sau đây:
a. Tìm kiếm phần tử có giá trị x trong list với x được nhập từ bàn phím, nếu có
hãy in ra vị trí xác định của x trong list.

b. Chỉnh sửa lại giá trị của một phần tử x được tìm thấy ở câu a, in danh sách
sau khi chỉnh sửa ra màn hình.

c. Thêm một phần tử có giá trị là y với y được nhập vào từ bàn phím (vị trí đầu,
cuối, giữa list).

d. Không sử dụng hàm sort(), sắp xếp các phần tử trong list theo giá trị giảm
dần. In ra màn hình danh sách trước và sau khi sắp xếp.

e. Xóa một phần tử bất kỳ trong list. In ra màn hình danh sách trước và sau khi
loại bỏ.
"""

list = []
while True:
    x = int(input("Nhap x: "))
    list.append(x)
    if x == 0:
        break
print(list)
a = int(input("Nhap x can tim: "))
if a in list:
    print("Vi tri cua x la: ", list.index(a))
else:
    print("Khong tim thay x trong list")


b = int(input("Nhap x can chinh sua: "))
list[list.index(b)] = int(input("Nhap x moi: "))
print(list)


c = int(input("Nhap x can them: "))
list.insert(list.index(c), int(input("Nhap x moi: ")))
print(list)
list.sort()
print(list)

d = list.copy()
d.sort(reverse=True)
print(d)

e = int(input("Nhap x can xoa: "))
list.remove(e)
print(list)
