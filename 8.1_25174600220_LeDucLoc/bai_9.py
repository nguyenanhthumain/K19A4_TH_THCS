#xây dựng hàm
def tinh_so_hoc(a, b):
    print(f"\n--- Kết quả số học giữa {a} và {b} ---")
    print(f"Tổng (a + b): {a + b}")
    print(f"Hiệu (a - b): {a - b}")
    print(f"Tích (a * b): {a * b}")

    if b != 0:
        print(f"Thương (a/b): {a/b}")
    else:
        print("Thương (a/b): Không thể chia cho 0!")


def tinh_luy_thua_1(a, b, n):
    ket_qua = a ** (b + n)
    return ket_qua


def tinh_luy_thua_2(a, b, n):
    so_mu = n + (2 ** a)
    ket_qua = b ** so_mu
    return ket_qua

#chương trình chính
def main():
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    n = float(input("Nhập số n: "))

    tinh_so_hoc(a, b)

    res1 = tinh_luy_thua_1(a, b, n)
    print(f"Giá trị a^(b + n) là: {res1}")
    
    res2 = tinh_luy_thua_2(a, b, n)
    print(f"Giá trị b^(n + 2^a) là: {res2}")

if __name__ == "__main__":
    main()