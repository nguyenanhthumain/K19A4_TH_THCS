def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def tim_bcnn(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // tim_ucln(a, b)

def rut_gon_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau == 0:
        print("Mẫu số phải khác 0.")
        return
    ucln = tim_ucln(tu, mau)
    print(f"Phân số rút gọn: {tu//ucln}/{mau//ucln}")

def tim_min_max():
    n = int(input("Nhập số lượng phần tử n: "))
    if n <= 0: return
    ds = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(n)]
    print(f"Số lớn nhất: {max(ds)}, Số nhỏ nhất: {min(ds)}")