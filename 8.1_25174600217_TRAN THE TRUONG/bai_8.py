PI = 3.14

# Hình tròn
def hinh_tron():
    r = float(input("Nhập bán kính hình tròn r: "))
    if r <= 0:
        print("Bán kính phải > 0")
        return
    chu_vi = 2 * PI * r
    dien_tich = PI * r * r
    print("Hình tròn: Chu vi =", chu_vi, ", Diện tích =", dien_tich)


# Hình vuông
def hinh_vuong():
    a = float(input("Nhập cạnh hình vuông a: "))
    if a <= 0:
        print("Cạnh phải > 0")
        return
    chu_vi = 4 * a
    dien_tich = a * a
    print("Hình vuông: Chu vi =", chu_vi, ", Diện tích =", dien_tich)


# Hình chữ nhật
def hinh_chu_nhat():
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    if a <= 0 or b <= 0:
        print("Chiều dài và chiều rộng phải > 0")
        return
    chu_vi = 2 * (a + b)
    dien_tich = a * b
    print("Hình chữ nhật: Chu vi =", chu_vi, ", Diện tích =", dien_tich)


# Hình tam giác
def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Các cạnh phải > 0")
        return
    if a + b <= c or a + c <= b or b + c <= a:
        print("Ba cạnh không tạo thành tam giác")
        return

    chu_vi = a + b + c
    p = chu_vi / 2

    t = p * (p - a) * (p - b) * (p - c)
    if t <= 0:
        print("Không tính được diện tích (số liệu không hợp lệ)")
        return

    x = t
    for i in range(20):
        x = (x + t / x) / 2

    dien_tich = x
    print("Hình tam giác: Chu vi =", chu_vi, ", Diện tích xấp xỉ =", dien_tich)


def main():
    print("=== TÍNH CHU VI VÀ DIỆN TÍCH CÁC HÌNH ===")
    hinh_tron()
    hinh_vuong()
    hinh_chu_nhat()
    hinh_tam_giac()


main()