import random
def kt_nguyento(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def so_thoa_man():
    n = int(input("Nhập độ dài danh sách n: "))
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print(f"Danh sách ngẫu nhiên: {danh_sach}")
    print(f"Các số nguyên tố có trong danh sách là:", end=" ")
    co_so_nguyento = False
    for x in danh_sach:
        if kt_nguyento(x):
            print(x, end=" ")
            co_so_nguyento = True
    if not co_so_nguyento:
        print(f"Không có số nguyên tố nào.")
    print() 
so_thoa_man()
