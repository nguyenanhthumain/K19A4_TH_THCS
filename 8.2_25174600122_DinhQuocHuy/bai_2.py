import random

def tao_danh_sach_binh_phuong(n):
    
    danh_sach = [random.randint(1, 100) for _ in range(n)]
  
    binh_phuong = lambda x: x ** 2
   
    ket_qua = list(map(binh_phuong, danh_sach))
    return danh_sach, ket_qua

try:
    n = int(input("Nhập độ dài danh sách n: "))
    if n <= 0:
        print("Vui lòng nhập n > 0")
    else:
        ds_goc, ds_binh_phuong = tao_danh_sach_binh_phuong(n)
        print("Danh sách gốc:", ds_goc)
        print("Danh sách bình phương:", ds_binh_phuong)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")