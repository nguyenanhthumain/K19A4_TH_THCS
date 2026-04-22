def value(x):
    return x + 1

def in_so_ke_tiep():
    n = int(input("Nhập một số nguyên: "))
    so_tiep = value(n)
    print(f"Số kế tiếp của {n} là: {so_tiep}")

in_so_ke_tiep()