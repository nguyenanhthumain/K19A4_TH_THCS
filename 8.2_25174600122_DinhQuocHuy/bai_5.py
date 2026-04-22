import random

def tao_danh_sach_kiem_tra_chan(n):
    danh_sach = [random.randint(1, 100) for _ in range(n)]
   
    la_chan = lambda x: x % 2 == 0
    ket_qua = list(map(la_chan, danh_sach))
    return danh_sach, ket_qua


try:
    n = int(input("Nhập độ dài danh sách n: "))
    if n <= 0:
        print("Vui lòng nhập n > 0")
    else:
        ds, check = tao_danh_sach_kiem_tra_chan(n)
        print("Danh sách:", ds)
        print("Kết quả kiểm tra chẵn (True = chẵn, False = lẻ):", check)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")