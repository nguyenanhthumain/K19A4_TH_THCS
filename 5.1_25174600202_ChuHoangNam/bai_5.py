#cau5
n = int(input("Nhập n: "))
day_so = list(range(1, n + 1))
so_nguyen_to = []
so_hoan_hao = []
for so in day_so:
    if so > 1:
        dem_uoc = 0
        for i in range(1, so + 1):
            if so % i == 0:
                dem_uoc += 1
        if dem_uoc == 2:
            so_nguyen_to.append(so)
            
    tong_uoc = 0
    for j in range(1, so):
        if so % j == 0:
            tong_uoc += j
    if tong_uoc == so and so != 0:
        so_hoan_hao.append(so)
print("Số nguyên tố:", so_nguyen_to)
print("Số hoàn hảo:", so_hoan_hao)