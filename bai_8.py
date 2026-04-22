def hinh_tron(r):
    return 2*3.14*r, 3.14*r*r

def hinh_vuong(a):
    return 4*a, a*a

def hcn(a, b):
    return 2*(a+b), a*b

def tam_giac(a, b, c):
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    return a+b+c, S

print("1. Hình tròn")
print("2. Hình vuông")
print("3. HCN")
print("4. Tam giác")

chon = int(input("Chọn: "))

if chon == 1:
    r = float(input("r = "))
    cv, dt = hinh_tron(r)
    print("Chu vi:", cv, "Diện tích:", dt)

elif chon == 2:
    a = float(input("a = "))
    cv, dt = hinh_vuong(a)
    print("Chu vi:", cv, "Diện tích:", dt)

elif chon == 3:
    a = float(input("a = "))
    b = float(input("b = "))
    cv, dt = hcn(a, b)
    print("Chu vi:", cv, "Diện tích:", dt)

elif chon == 4:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    cv, dt = tam_giac(a, b, c)
    print("Chu vi:", cv, "Diện tích:", dt)