import random

def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def tao_danh_sach_va_in_nguyen_to(n):
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", danh_sach)
    print("Các số nguyên tố trong danh sách:")
    for so in danh_sach:
        if la_so_nguyen_to(so):
            print(so, end=" ")
    print() 


try:
    n = int(input("Nhập độ dài danh sách n: "))
    if n <= 0:
        print("Vui lòng nhập n > 0")
    else:
        tao_danh_sach_va_in_nguyen_to(n)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")