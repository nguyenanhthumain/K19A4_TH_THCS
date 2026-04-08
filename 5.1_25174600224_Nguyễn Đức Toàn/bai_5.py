n = int(input("Nhập n: "))

danh_sach = []
for so in range(1, n + 1):
    danh_sach += [so]

so_nguyen_to = []
for so in danh_sach:
    if so > 1:
        la_so_nguyen_to = True
        for i in range(2, so):
            if so % i == 0:
                la_so_nguyen_to = False
                break
        if la_so_nguyen_to:
            so_nguyen_to += [so]

so_hoan_hao = []
for so in danh_sach:
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i
    if tong_uoc == so:
        so_hoan_hao += [so] 

print("Danh sách số nguyên tố:", so_nguyen_to)
print("Danh sách số hoàn hảo:", so_hoan_hao)