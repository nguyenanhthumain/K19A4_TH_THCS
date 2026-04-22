def nhap_list():
    n = int(input("Nhập số phần tử: "))
    lst = []
    for i in range(n):
        x = int(input(f"Phần tử {i+1}: "))
        lst.append(x)
    return lst

def binh_phuong(lst):
    return list(map(lambda x: x*x, lst))

# chạy
lst = nhap_list()
kq = binh_phuong(lst)
print("List ban đầu:", lst)
print("Bình phương:", kq)