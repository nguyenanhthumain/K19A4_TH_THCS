#cau3
while True:
    m = int(input("Nhập m (m > 0): "))
    n = int(input("Nhập n (n > m): "))   
    if 0 < m < n:
        print("Dieu kien hop le")
        break  
    else:
        print("Loi! Dk: 0 < m < n khong thoa man , nhap lai ")
danh_sach_so = []
for i in range(m, n + 1):
    danh_sach_so.append(i)
def kiem_tra_so_chan(so):
    if so % 2 == 0:
        return True
    else:
        return False
ket_qua_filter = filter(kiem_tra_so_chan, danh_sach_so)
danh_sach_so_chan = list(ket_qua_filter)

print("Cac so chan trong khoang tu", m, "den", n, "la:")
print(danh_sach_so_chan)