import math
r = float(input("Nhập bán kính r để tính hình tròn: "))
if r > 0:
    cv_tron = 2 * math.pi * r
    dt_tron = math.pi * r**2
    print(f"Hình tròn : Chu vi: {cv_tron}, Diện tích: {dt_tron}")
else:
    print(f"Yêu cầu nhập lại")
canh_v = float(input("Nhập độ dài cạnh hình vuông: "))
if canh_v > 0:
    print(f"Hình vuông : Chu vi: {canh_v * 4}, Diện tích: {canh_v**2}")
else:
    print(f"Yêu cầu nhập lại")
dai = float(input("Nhập chiều dài hình chữ nhật: "))
rong = float(input("Nhập chiều rộng hình chữ nhật: "))
if dai > 0 and rong > 0:
    print(f"Hình chữ nhật : Chu vi: {(dai + rong) * 2}, Diện tích: {dai * rong}")
else:
    print(f"Yêu cầu nhập lại")
a = float(input("Nhập cạnh a hình tam giác: "))
b = float(input("Nhập cạnh b hình tam giác: "))
c = float(input("Nhập cạnh c hình tam giác: "))
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    cv_tg = a + b + c
    p = cv_tg / 2
    dt_tg = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Hình tam giác : Chu vi: {cv_tg}, Diện tích: {dt_tg}")
else:
    print(f"Yêu cầu nhập lại")
