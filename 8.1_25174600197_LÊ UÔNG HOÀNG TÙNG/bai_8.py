import math
def hinh_tron(r):
    if r <= 0:
        print("ban kinh khong hop le")
        return
    cv = 2 * math.pi * r
    dt = math.pi * r * r
    print("chu vi =", cv)
    print("dien tich =", dt)
def hinh_vuong(a):
    if a <= 0:
        print("canh khong hop le")
        return
    print("chu vi =", 4*a)
    print("dien tich =", a*a)
def hinh_chu_nhat(a, b):
    if a <= 0 or b <= 0:
        print("kich thuoc khong hop le")
        return
    print("chu vi =", 2*(a+b))
    print("dien tich =", a*b)
def hinh_tam_giac(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("khong phai tam giac")
        return
    p = (a + b + c) / 2
    dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("chu vi =", a+b+c)
    print("dien tich =", dt)
def bai_8():
    r = float(input("ban kinh: "))
    hinh_tron(r)
    a = float(input("canh vuong: "))
    hinh_vuong(a)
    a = float(input("dai: "))
    b = float(input("rong: "))
    hinh_chu_nhat(a,b)
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    hinh_tam_giac(a,b,c)
bai_8()