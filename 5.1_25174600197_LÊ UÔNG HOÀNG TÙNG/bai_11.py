#bai11
n = int(input("nhap so luong tuple cho moi danh sach: "))
print("\nnhap danh sach kiem tra (test_list):")
test_list = []
for i in range(n):
    print(f"tuple thu {i+1}:")
    a = int(input("  nhap phan tu thu 1: "))
    b = int(input("  nhap phan tu thu 2: "))
    test_list.append((a, b))
print("\nnhap danh sach tim kiem (search_tup):")
search_tup = []
for i in range(n):
    print(f"tuple thu {i+1}:")
    a = int(input("  nhap phan tu thu 1: "))
    b = int(input("  nhap phan tu thu 2: "))
    search_tup.append((a, b))
print("\ntest_list :", test_list)
print("search_tup:", search_tup)
print("\nket qua tim kiem:")
for i in range(len(search_tup)):
    if search_tup[i] in test_list:
        vitri = test_list.index(search_tup[i])
        print(f"tuple {search_tup[i]} xuat hien tai vi tri {vitri} trong test_list")
    else:
        print(f"tuple {search_tup[i]} khong co trong test_list")
        