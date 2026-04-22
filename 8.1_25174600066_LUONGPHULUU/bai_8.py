# Hình tròn
def tinh_hinh_tron():
    r = float(input("Nhập bán kính: "))
    if r <= 0:
        print("Dữ liệu không hợp lệ")
        return
    cv = 2 * 3.14 * r
    dt = 3.14 * r * r
    print("Chu vi:", cv)
    print("Diện tích:", dt)

# Hình vuông
def tinh_hinh_vuong():
    a = float(input("Nhập cạnh: "))
    if a <= 0:
        print("Dữ liệu không hợp lệ")
        return
    print("Chu vi:", 4 * a)
    print("Diện tích:", a * a)

# Hình chữ nhật
def tinh_hcn():
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    if dai <= 0 or rong <= 0:
        print("Dữ liệu không hợp lệ")
        return
    print("Chu vi:", 2 * (dai + rong))
    print("Diện tích:", dai * rong)

# Hình tam giác
def tinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a <= 0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b or b+c <= a:
        print("Tam giác không hợp lệ")
        return
    p = (a + b + c) / 2
    dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Chu vi:", a + b + c)
    print("Diện tích:", dt)
# ===== Gọi chương trình =====
print("Hình tròn:")
tinh_hinh_tron()
print("\nHình vuông:")
tinh_hinh_vuong()
print("\nHình chữ nhật:")
tinh_hcn()
print("\nHình tam giác:")
tinh_tam_giac()