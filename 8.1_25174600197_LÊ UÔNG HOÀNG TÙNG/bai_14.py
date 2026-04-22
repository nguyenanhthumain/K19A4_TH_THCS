def bai_14():
    n = int(input("nhap so phan tu: "))
    ds = []
    for i in range(n):
        ds.append(int(input("nhap so: ")))
    ds_binh_phuong = list(map(lambda x: x*x, ds))
    print("list ban dau:", ds)
    print("list binh phuong:", ds_binh_phuong)
bai_14()