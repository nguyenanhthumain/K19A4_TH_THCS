#Bai3
while True:
    m = int(input("nhap m: "))
    n = int(input("nhap n: "))
    
    if m > 0 and n > m:
        break
    else:
        print("dieu kien khong thoa man, nhap lai (0 < m < n)")
numbers = list(range(m, n+1))
so_chan = list(filter(lambda x: x % 2 == 0, numbers))
print("danh sach tu", m, "den", n, ":", numbers)
print("cac so chan:", so_chan)