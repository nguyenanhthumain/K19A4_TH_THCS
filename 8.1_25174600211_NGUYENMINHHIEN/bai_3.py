# a) 
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# b)
def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
# c)
def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]
while True:
    print("\n===== MENU BAI 3 =====")
    print("1. Kiem tra so nguyen to")
    print("2. Kiem tra so hoan hao")
    print("3. In so doi xung (0 -> 999)")
    print("0. Thoat")
    chon = input("Nhap lua chon: ")
    if chon == "1":
        n = int(input("Nhap n: "))
        if la_so_nguyen_to(n):
            print(n, "la so nguyen to")
        else:
            print(n, "khong phai so nguyen to")
    elif chon == "2":
        n = int(input("Nhap n: "))
        if la_so_hoan_hao(n):
            print(n, "la so hoan hao")
        else:
            print(n, "khong phai so hoan hao")
    elif chon == "3":
        dem = 0
        for i in range(1000):
            if la_so_doi_xung(i):
                print(f"{i:5}", end="")
                dem += 1
                if dem % 15 == 0:
                    print()
    elif chon == "0":
        print("Ket thuc chuong trinh")
        break
    else:
        print("Lua chon khong hop le!")