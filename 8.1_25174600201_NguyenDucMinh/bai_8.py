import math

def hinh_tron():
    r = float(input("Nhập bán kính: "))
    if r <= 0:
        print("Không hợp lệ")
        return
    print("Chu vi:", 2 * math.pi * r)
    print("Diện tích:", math.pi * r * r)

def hinh_vuong():
    a = float(input("Nhập cạnh: "))
    if a <= 0:
        print("Không hợp lệ")
        return
    print("Chu vi:", 4 * a)
    print("Diện tích:", a * a)

def hinh_chu_nhat():
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    if a <= 0 or b <= 0:
        print("Không hợp lệ")
        return
    print("Chu vi:", 2 * (a + b))
    print("Diện tích:", a * b)

def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Không phải tam giác hợp lệ")
        return

    p = (a + b + c) / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print("Chu vi:", a + b + c)
    print("Diện tích:", dien_tich)


# MENU chọn hình
print("1. Hình tròn")
print("2. Hình vuông")
print("3. Hình chữ nhật")
print("4. Hình tam giác")

chon = int(input("Chọn hình: "))

if chon == 1:
    hinh_tron()
elif chon == 2:
    hinh_vuong()
elif chon == 3:
    hinh_chu_nhat()
elif chon == 4:
    hinh_tam_giac()
else:
    print("Lựa chọn không hợp lệ")