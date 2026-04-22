#cau8
PI = 3.14

#tron
r = float(input("Nhap ban kinh hinh tron: "))
if r > 0:
    print(f"Chu vi hinh tron: {2 * PI * r}")
    print(f"Dien tich hinh tron: {PI * r * r}")
else: print("Ban kinh phai > 0")

#vuong
canh = float(input("Nhap canh hinh vuong: "))
if canh > 0:
    print(f"Chu vi: {4 * canh}, Dien tich: {canh * canh}")

#chu nhat
dai = float(input("Nhap chieu dai: "))
rong = float(input("Nhap chieu rong: "))
if dai > 0 and rong > 0:
    print(f"Chu vi: {2 * (dai + rong)}, Dien tich: {dai * rong}")

#tam giac
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))
if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    print(f"Chu vi: {p}")
    nua_p = p / 2
    s = (nua_p * (nua_p - a) * (nua_p - b) * (nua_p - c)) ** 0.5
    print(f"Dien tich: {s}")
else: print("3 canh khong tao thanh tam giac!")