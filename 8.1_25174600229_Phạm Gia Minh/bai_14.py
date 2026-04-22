def bai_14():
    n = int(input("Nhập n: "))
    danh_sach = []
    for i in range(n):
        so = int(input(f"Nhập số {i+1}: "))
        danh_sach.append(so)
    
    list_binh_phuong = list(map(lambda x: x**2, danh_sach))
    
    print(danh_sach)
    print(list_binh_phuong)

