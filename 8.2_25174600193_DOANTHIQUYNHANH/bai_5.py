import random

def kiem_tra_chan(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", ds)

    ket_qua = list(map(lambda x: x % 2 == 0, ds))
    print("Kết quả (True = chẵn, False = lẻ):", ket_qua)


n = int(input("Nhập n: "))
kiem_tra_chan(n)