import random
def ktr_phan_tu():
    n = int(input("Nhập độ dài danh sách n: "))
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print(f"Danh sách ngẫu nhiên: {danh_sach}")
    ket_qua = list(map(lambda x: x % 2 == 0, danh_sach))
    print(f"Kết quả kiểm tra (True=Chẵn, False=Lẻ): {ket_qua}")
ktr_phan_tu()
