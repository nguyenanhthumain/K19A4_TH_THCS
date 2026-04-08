n = int(input("Nhập n: "))

test_list = []
search_list = []

print("Nhập test_list:")
for i in range(n):
    a = int(input())
    b = int(input())
    test_list.append((a, b))

print("Nhập search_list:")
for i in range(n):
    a = int(input())
    b = int(input())
    search_list.append((a, b))

# tìm vị trí
for t in search_list:
    if t in test_list:
        print(t, "ở vị trí", test_list.index(t))