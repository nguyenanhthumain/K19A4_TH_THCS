"""6. Viết chương trình sinh một dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong
khoảng [1,99999]. Sau đó sắp xếp lại theo thứ tự tăng dần theo 2 cách. Sử dụng
hàm sorted() và không sử dụng hàm sorted()."""

#cách 1
A = []
for i in range(1000):
    so = (i * 327 + 543) % 100000 
    A.append(so)

print("Đã tạo xong danh sách A gồm 1000 phần tử.")
print("10 phần tử đầu tiên của A:", A[:10])

A_1 = A[:] 
A_1.sort()
print("10 số nhỏ nhất:", A_1[:10])






#cách 2
A_2 = A[:] 
n = len(A_2)

for i in range(n):
    chi_muc_min = i
    for j in range(i + 1, n):
        if A_2[j] < A_2[chi_muc_min]:
            chi_muc_min = j

    tam = A_2[i]
    A_2[i] = A_2[chi_muc_min]
    A_2[chi_muc_min] = tam
print("10 số nhỏ nhất:", A_2[:10])