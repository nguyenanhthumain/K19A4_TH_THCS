import random
def tao_danh_sach(n):
    danh_sach = [random.randint(1, 20) for _ in range(n)]
    kiem_tra_chan = lambda x: x % 2 == 0
    ket_qua = list(map(kiem_tra_chan, danh_sach))
    return danh_sach, ket_qua

n = int(input("Nhập số phần tử n: "))
ds, kq = tao_danh_sach(n)
print("Danh sách:", ds)
print("Kết quả (chẵn=True, lẻ=False):", kq)