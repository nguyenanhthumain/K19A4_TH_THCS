# Bai 7
# a) Tim ucln
def tim_uoc_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# b) Tim bcnn
def tim_boi_chung_nho_nhat(a, b):
    return a * b // tim_uoc_chung_lon_nhat(a, b)
# c) Rut gon phan so
def rut_gon_phan_so(tu, mau):
    g = tim_uoc_chung_lon_nhat(tu, mau)
    return tu//g, mau//g

# d) Tim min max
def tim_so_nho_nhat_va_lon_nhat(ds):
    return min(ds), max(ds)


print("=== Bai 7 ===")

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print("UCLN:", tim_uoc_chung_lon_nhat(a, b))
print("BCNN:", tim_boi_chung_nho_nhat(a, b))

tu = int(input("Nhap tu: "))
mau = int(input("Nhap mau: "))
print("Rut gon:", rut_gon_phan_so(tu, mau))

n = int(input("Nhap so luong: "))
ds = []
for i in range(n):
    ds.append(int(input()))

print("Min max:", tim_so_nho_nhat_va_lon_nhat(ds))