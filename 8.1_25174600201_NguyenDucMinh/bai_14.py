n = int(input("Nhập số lượng phần tử: "))

lst = []

for i in range(n):
    x = int(input("Nhập số: "))
    lst.append(x)

square_list = []

for x in lst:
    square_list.append(x * x)

print("List ban đầu:", lst)
print("List bình phương:", square_list)