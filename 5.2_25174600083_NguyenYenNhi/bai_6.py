#bai_6
"""
Viết chương trình sinh một dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong
khoảng [1,99999]. Sau đó sắp xếp lại theo thứ tự tăng dần theo 2 cách. Sử dụng
hàm sorted() và không sử dụng hàm sorted().
"""


list_A = []

while len(list_A) < 1000:
    x = int(input("Nhập số: "))
    if 1 <= x <= 99999:
        list_A.append(x)
    else:
        print("Nhập lại (1 → 99999)")

print("List ban đầu:", list_A)
list_A_sorted = sorted(list_A)
print("List sau khi sắp xếp (sử dụng sorted()):", list_A_sorted[:10])

for i in range(len(list_A)):
    for j in range(i + 1, len(list_A)):
        if list_A[i] > list_A[j]:
            list_A[i], list_A[j] = list_A[j], list_A[i]
print("List sau khi sắp xếp (không sử dụng sorted()):", list_A[:10])