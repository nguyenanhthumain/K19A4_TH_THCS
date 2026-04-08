#Bài 11:
"""11. Giả sử có hai danh sách là danh sách kiểm tra (test_list) chứa các phần tử là
tuple và một danh sách các tuple tìm kiếm (search_tup), ví dụ: test_list = [(4,5),
(7,6), (1,0), (3,4)], search_tup = [(3,4), (8,9), (7,6), (1,2)]. Yêu cầu:

• Tạo hai dach sách trên với các phần tử được nhập từ bàn phím, trong đó mỗi
danh sách có n (nhập từ bàn phím) phần tử tuple, mỗi tuple có 2 phần tử.
Mỗi giá trị của tuple là một số tự nhiên được nhập từ bàn phím.
• Viết chương trình tìm chỉ mục của các cặp tuple trong danh sách tìm kiếm
xuất hiện trong danh sách kiểm tra."""


n = int(input("Nhập số lượng phần tử n: "))

test_list = []
search_tup = []

for i in range(n):
    x = int(input("Nhap phan tu thu " + str(i + 1) + " cua test_list: "))
    y = int(input("Nhap phan tu thu " + str(i + 1) + " cua test_list: "))
    test_list.append((x, y))

for i in range(n):
    x = int(input("Nhap phan tu thu " + str(i + 1) + " cua search_tup: "))
    y = int(input("Nhap phan tu thu " + str(i + 1) + " cua search_tup: "))
    search_tup.append((x, y))

print("Cac cap tu trong search_tup xuat hien trong test_list:")
for i in search_tup:    
    if i in test_list:
        print(f"{i} xuat hien tai chi muc {test_list.index(i)} trong test_list")