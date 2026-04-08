n = int(input("Nhập số lượng phần tử n: "))
test_list = []
print("Nhập các tuple cho test_list:")
for i in range(n):
    print(f"Tuple thứ {i}:")
    a = int(input("  Nhập phần tử 1: "))
    b = int(input("  Nhập phần tử 2: "))
    test_list.append((a, b))
search_tup = []
print("Nhập các tuple cho search_tup:")
for i in range(n):
    print(f"Tuple thứ {i}:")
    a = int(input("  Nhập phần tử 1: "))
    b = int(input("  Nhập phần tử 2: "))
    search_tup.append((a, b))
print("test_list:", test_list)
print("search_tup:", search_tup)
print("Kết quả tìm kiếm:")
for i in range(len(search_tup)):
    found = False
    for j in range(len(test_list)):
        if search_tup[i] == test_list[j]:
            print(f"{search_tup[i]} xuất hiện tại vị trí {j} trong test_list")
            found = True
            break
    if not found:
        print(f"{search_tup[i]} không xuất hiện trong test_list")