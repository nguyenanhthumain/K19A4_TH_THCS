def a(r):
    pi = 3.14
    chu_vi = 2 * pi * r
    dien_tich = pi * r * r
    return chu_vi, dien_tich

def hinh_tron():
    r = float(input("Nhập bán kính: "))
    if r <= 0:
        print("Yêu cầu nhập lại")
        return
    cv, dt = a(r)
    print("Chu vi =", cv)
    print("Diện tích =", dt)
hinh_tron()

def b(a):
    chu_vi = 4 * a
    dien_tich = a * a
    return chu_vi, dien_tich


def hinh_vuong():
    a = float(input("Nhập cạnh hình vuông: "))
    if a <= 0:
        print("Không hợp lệ")
        return
    cv, dt = b(a)
    print("Chu vi =", cv)
    print("Diện tích =", dt)
hinh_vuong()


def c(a, b):
    chu_vi = 2 * (a + b)
    dien_tich = a * b
    return chu_vi, dien_tich

def hinh_chu_nhat():
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    if a <= 0 or b <= 0:
        print("Yêu cầu nhập lại")
        return
    cv, dt = c(a, b)
    print("Chu vi =", cv)
    print("Diện tích =", dt)
hinh_chu_nhat()


def d(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return None, None
    chu_vi = a + b + c
    p = chu_vi / 2
    dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return chu_vi, dien_tich

def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a <= 0 or b <= 0 or c <= 0:
        print("Yêu cầu nhập lại")
        return  
    cv, dt = d(a, b, c) 
    if cv is None:
        print("Không phải tam giác")
    else:
        print("Chu vi =", cv)
        print("Diện tích =", dt)
hinh_tam_giac()