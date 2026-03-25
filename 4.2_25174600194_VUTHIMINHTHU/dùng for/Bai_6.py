n = input("Nhập một số lớn hơn 100: ")
if int(n) <= 100:
    print("Yêu cầu nhập lại")
else:
    tong = 0
    for so in n:
        tong += int(so)
    print(f"Tổng các chữ số của {n} là: {tong}")
