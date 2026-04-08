def la_so_chan(x):
    return x % 2 == 0
while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhâp n: "))
    if 0 < m < n:
        break
    else:
        print("Lỗi!Yêu cầu nhập lại!")
lst =  list(range(m, n + 1))
so_chan = list(filter(la_so_chan, lst))
print("Danh sách ban đầu:", lst)
print("Các số chẵn:", so_chan)