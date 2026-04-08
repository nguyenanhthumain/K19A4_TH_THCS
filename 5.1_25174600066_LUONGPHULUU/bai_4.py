while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhâp n: "))
    if 0 < m < n:
        break
    else:
        print("Lỗi!Yêu cầu nhập lại!")
lst = list(range(m, m + 200, 2))[:100]
tong = sum(lst)
print("Danh sách ban đầu:", lst)
print("Tổng các số:", tong)