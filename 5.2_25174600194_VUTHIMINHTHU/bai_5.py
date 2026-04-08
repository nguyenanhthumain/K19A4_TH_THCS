import random
lst_A = []
while len(lst_A) < 1000:
    so_ngau_nhien = random.randint(1, 99999)
    if so_ngau_nhien % 7 != 0:
        lst_A.append(so_ngau_nhien)
print("Giá trị thoả mã trong danh sách:", lst_A[1:1000])