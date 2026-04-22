#a.
def ucln(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

#b.
def bcnn(a, b):
    return (a * b) // ucln(a, b)

#c.
def rut_gon_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))

    if mau == 0:
        print("Phân số không hợp lệ (mẫu = 0)")
        return

    u = ucln(abs(tu), abs(mau))
    print("Phân số rút gọn là:", tu // u, "/", mau // u)

#d.
def tim_min_max():
    n = int(input("Nhập số lượng phần tử n: "))

    so = int(input("Nhập số thứ 1: "))
    min_val = so
    max_val = so

    for i in range(2, n + 1):
        so = int(input(f"Nhập số thứ {i}: "))
        if so < min_val:
            min_val = so
        if so > max_val:
            max_val = so

    print("Số nhỏ nhất là:", min_val)
    print("Số lớn nhất là:", max_val)


def main():
    print("a:")
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("UCLN =", ucln(a, b))

    print("\nb:")
    print("BCNN =", bcnn(a, b))

    print("\nc:")
    rut_gon_phan_so()

    print("\nd:")
    tim_min_max()


main()