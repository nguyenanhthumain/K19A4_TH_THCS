#bai_7
"""
a) Viết chương trình tìm ước chung lớn nhất của 2 số a, b.
b) Xây chương trình tìm bội chung nhỏ nhất của 2 số a, b.
c) Viết chương trình cho phép thực hiện rút gọn phân số.
Hướng dẫn:
+ Tìm UCLN của tử số và mẫu số.
+ Chia tử và mẫu của phân số cho UCLN vừa tìm được.
d) Viết chương trình nhập vào n số nguyên và in ra các số nhỏ nhất và lớn nhất
trong các số đó.
"""

def ucln(a, b):
    while b != 0:
        a=b 
        b=a % b
    return a

def bcnn(a, b):
    return a * b // ucln(a, b)

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f"ƯCLN của {a} và {b} là: {ucln(a, b)}")
print(f"BCNN của {a} và {b} là: {bcnn(a, b)}")

def rut_gon_phan_so(tu,mau):
    ucln_tu_mau = ucln(tu,mau)
    tu_rut_gon = tu // ucln_tu_mau
    mau_rut_gon = mau // ucln_tu_mau
    return tu_rut_gon, mau_rut_gon
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu_rut_gon, mau_rut_gon = rut_gon_phan_so(tu, mau)
print("Phân số sau khi rút gọn: ",rut_gon_phan_so(tu, mau))
rut_gon_phan_so(tu, mau)

n = int(input("Nhập số lượng số nguyên: "))
so_nguyen = []
for i in range(n):
    so = int(input(f"Nhập số nguyên thứ {i+1}: "))
    so_nguyen.append(so)
min_so = min(so_nguyen)
max_so = max(so_nguyen)
print(f"Số nguyên nhỏ nhất và lớn nhất là: {min_so} và {max_so}")