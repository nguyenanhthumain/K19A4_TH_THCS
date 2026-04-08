n = int(input("Nhập số phần tử danh sách: "))

test_list = []
print("Nhập danh sách kiểm tra: ")
for i in range(n):
    a = int(input(f"Phần tử {i+1}, phần tử thứ 1 của tuple: "))
    b = int(input(f"Phần tử {i+1}, phần tử thứ 2 của tuple: "))
    test_list += [(a, b)]

search_tup = []
print("Nhập danh sách tìm kiếm: ")
for i in range(n):
    a = int(input(f"Phần tử {i+1}, phần tử thứ 1 của tuple: "))
    b = int(input(f"Phần tử {i+1}, phần tử thứ 2 của tuple: "))
    search_tup += [(a, b)]

print("\nKết quả:")
for index in range(len(search_tup)):
    if search_tup[index] in test_list:
        print(f"Tuple {search_tup[index]} xuất hiện tại chỉ mục {index} trong search_tup")