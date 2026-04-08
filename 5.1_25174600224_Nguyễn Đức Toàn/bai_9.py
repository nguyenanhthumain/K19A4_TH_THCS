m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

if not (0 < m < n):
    print("Yêu cầu nhập lại")
else:
    tuple_goc = tuple(range(m, n + 1))
    print("Tuple gốc:", tuple_goc)
    do_dai = len(tuple_goc)
    mid = do_dai // 2
    tp1 = tuple_goc[:mid]
    tp2 = tuple_goc[mid:]

    print("Nửa đầu :", tp1)
    print("Nửa sau :", tp2)
