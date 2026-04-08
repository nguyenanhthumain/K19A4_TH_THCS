#Bai4
m = int(input("nhap m: "))
n = int(input("nhap n: "))
while not (m > 0 and n > m):
    print("dieu kien khong thoa man, nhap lai (0 < m < n)")
    m = int(input("nhap m: "))
    n = int(input("nhap n: "))
danhsach = []
i = m
while len(danhsach) < 100 and i <= n:
    if i % 2 == 0:           
        danhsach.append(i)
    i += 1
print("danh sach:", danhsach)
print("tong cac so:", sum(danhsach))