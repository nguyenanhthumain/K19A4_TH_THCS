def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def tim_bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // tim_ucln(a, b)
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ucln = tim_ucln(a, b)
print(f"a.Ước chung lớn nhất của {a} và {b} là: {ucln}")
bcnn = tim_bcnn(a, b)
print(f"b.Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")
if b == 0:
    print("c.Mẫu số bằng 0, không thể rút gọn phân số.")
else:
    tu_so_moi = a // ucln
    mau_so_moi = b // ucln
    print(f"c.Phân số {a}/{b} sau khi rút gọn là: {tu_so_moi}/{mau_so_moi}")
print("-" * 30)
n = int(input("d.Nhập số lượng phần tử n: "))
if n > 0:
    so = int(input("Nhập số thứ 1: "))
    so_lon_nhat = so
    so_nho_nhat = so
    for i in range(2, n + 1):
        so = int(input(f"Nhập số thứ {i}: "))
        if so > so_lon_nhat:
            so_lon_nhat = so
        if so < so_nho_nhat:
            so_nho_nhat = so
    print(f"Số lớn nhất là: {so_lon_nhat}")
    print(f"Số nhỏ nhất là: {so_nho_nhat}")
else:
    print("Số lượng phần tử không hợp lệ.")
