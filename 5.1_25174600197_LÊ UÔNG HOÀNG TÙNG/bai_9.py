# bai9
m = int(input("nhap m: "))
n = int(input("nhap n: "))
while not (m > 0 and n > m):
    print("dieu kien khong thoa man, nhap lai (0 < m < n)")
    m = int(input("nhap m: "))
    n = int(input("nhap n: "))
tpl = tuple(range(m, n+1))
print("tuple goc:", tpl)
do_dai = len(tpl)
giua = do_dai // 2
tp1 = tpl[:giua]      
tp2 = tpl[giua:]      
print("tp1 (nua dau):", tp1)
print("tp2 (nua cuoi):", tp2)