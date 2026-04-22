#bai_5
"""
Hãy viết hàm tạo 1 danh sách có độ dài là n với n nhập từ bàn phím với
các phần tử trong danh sách đó được khởi tạo ngẫu nhiên (được phép sử dụng
hàm random trong Python) và sử dụng lambda để trả về True nếu số đó là chẵn,
ngược lại trả về False.
"""
import random
def tao_danh_sach(n):
    n = int(input("Nhập độ dài danh sách: "))
    ds = []
    for i in range(n):
        so_phan_tu = random.randint(1, 100)
        ds.append(so_phan_tu)
    return ds

ds = tao_danh_sach(0)

kiem_tra_chan_le = lambda x: x % 2 == 0
ds_binh_phuong = []
for so in ds:
    if kiem_tra_chan_le(so):
        print(f"Số {so} là số chẵn.")
    else:
        print(f"Số {so} là số lẻ.")
