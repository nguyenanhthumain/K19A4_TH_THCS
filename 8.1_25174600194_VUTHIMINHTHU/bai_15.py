from functools import reduce
list_chan_100 = list(range(2, 101, 2))
print(f"a) Danh sách các số chẵn từ 1 đến 100:\n{list_chan_100}")
print("-" * 30)
n = int(input("b) Nhập số n: "))
danh_sach = list(range(1, n + 1))
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach))
if so_chan:
    tong_chan = reduce(lambda x, y: x + y, so_chan)
else:
    tong_chan = 0 
print(f"Các số chẵn trong danh sách: {so_chan}")
print(f"Tổng các số chẵn là: {tong_chan}")
