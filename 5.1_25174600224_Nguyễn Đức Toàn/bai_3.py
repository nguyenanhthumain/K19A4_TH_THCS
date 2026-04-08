while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))

    if 0 < m < n:
        break
    else:
        print("Yêu cầu nhập lại: ")

danh_sach = list(range(m, n + 1))

def la_so_chan(i):
    return i % 2 == 0
danh_sach_chan = list(filter(la_so_chan, danh_sach))
print("Danh sách số chẵn:", danh_sach_chan)