def a():
    n = int(input("Nhập số phần tử n: "))
    ds = []
    for i in range(n):
        x = int(input("Nhập số thứ " + str(i+1) + ": "))
        ds.append(x)
    binh_phuong = list(map(lambda x: x * x, ds))
    print("Danh sách ban đầu:", ds)
    print("Bình phương:", binh_phuong)
a()