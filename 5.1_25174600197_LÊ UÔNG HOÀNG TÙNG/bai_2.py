#Bai2
n = int(input("nhap n: "))
while n < 1:
    print("n phai lon hon hoac bang 1, nhap lai")
    n = int(input("nhap n: "))
m = int(input("nhap m: "))
danhsach = [i**2 for i in range(1, n+1)]
print("danh sach binh phuong:", danhsach)
if m >= n:
    print("danh sach ket qua:", [])
else:
    print("danh sach tru", m, "phan tu dau tien:", danhsach[m:])