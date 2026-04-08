m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
gia_tri = tuple(range(m, n+1))
gia_tri_giua = len(gia_tri)//2
tp1 = gia_tri[:gia_tri_giua]
tp2 = gia_tri[gia_tri_giua:]
print("tp1:", tp1)
print("tp2:", tp2)