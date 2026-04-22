#a)
def kiem_tra_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))

    if n < 2:
        print(n, "không phải là số nguyên tố")
        return

    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1

    if dem == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

#b)
def kiem_tra_hoan_hao():
    n = int(input("Nhập số nguyên dương n để kiểm tra số hoàn hảo: "))

    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i

    if tong == n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải là số hoàn hảo")

#c)
def in_so_doi_xung():
    print("\nCác số đối xứng trong phạm vi 1000:")

    dem = 0 

    for n in range(1000):
        s = str(n)
        if s == s[::-1]: 
            print(f"{n:5}", end="")
            dem += 1

            if dem == 15:
                print()
                dem = 0


def main():
    print("a)")
    kiem_tra_nguyen_to()

    print("\nb)")
    kiem_tra_hoan_hao()

    print("\nc)")
    in_so_doi_xung()

main()