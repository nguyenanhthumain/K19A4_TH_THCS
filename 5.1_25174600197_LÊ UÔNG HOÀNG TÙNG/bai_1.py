#Bai1
n = int(input("nhap n: "))
while n < 1:
    print("n phai lon hon hoac bang 1, nhap lai")
    n = int(input("nhap n: "))
m = int(input("nhap m: "))
danhsach = []
for i in range(1, n+1):
    danhsach.append(i**2)
print("danh sach binh phuong:", danhsach)
if m >= n:
    print("in toan bo danh sach:", danhsach)
else:
    print("in", m, "phan tu dau tien:", danhsach[:m])