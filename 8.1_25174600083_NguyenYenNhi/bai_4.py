#bai_4

def tinh_P(n) :
    p = 1
    for i in range(1,n + 1) :
        p = p*(2*i + 1)
    return p
n = int(input("Nhập n: "))
if n >= 0 :
    print("P(n) =", tinh_P(n))
else :
    print("n phải lớn hơn 0")

def tinh_S(n) :
    S = 1
    for i in range(1,n + 1) :
        S = S + (-1)**(i+1)
    return S
n = int(input("Nhập n: "))
if n >= 0 :
    print("S(n) =", tinh_S(n))
else :
    print("n phải lớn hơn 0")

def tinh_S(n) :
    S = 0
    for i in range(n + 1) :
        tong = 2
        for j in range(i + 1) :
            tong = tong + j 
        S = S + tong
    return S
n = int(input("Nhập n: "))
print("S(n) =", tinh_S(n))

def tinh_P() :
    x = float(input("Nhập x: "))
    y = float(input("Nhập y: "))
    n = int(input("Nhập n: "))
    if n <= 1 :
        print("n phải lớn hơn 1")
    else :
        print("Nhập lại")
    p = x**y
    P = 0
    for k in range(1,n + 1) :
        bieu_thuc = x+(32*y)+y**k
        P = p + bieu_thuc
print("P(x,y) =", tinh_P())