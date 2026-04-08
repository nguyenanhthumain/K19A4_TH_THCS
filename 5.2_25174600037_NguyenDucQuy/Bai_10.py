import random
ds_thoa_man = [i for i in range(201) if i % 35 == 0]
if ds_thoa_man:
    so_chon = random.choice(ds_thoa_man)
    print(f"Số ngẫu nhiên chia hết cho 5 và 7 trong khoảng 0-200 là: {so_chon}")