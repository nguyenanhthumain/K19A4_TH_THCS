n = int(input("Nhập n: "))

test_list = []
search_tup = []

print("Nhập test_list:")
for _ in range(n):
    a = int(input())
    b = int(input())
    test_list.append((a, b))

print("Nhập search_tup:")
for _ in range(n):
    a = int(input())
    b = int(input())
    search_tup.append((a, b))

result = []

for t in search_tup:
    if t in test_list:
        result.append(test_list.index(t))
    else:
        result.append(-1)
print(result)