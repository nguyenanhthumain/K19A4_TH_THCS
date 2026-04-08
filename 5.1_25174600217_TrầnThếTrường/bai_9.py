while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    print("Lỗi: Cần đảm bảo 0 < m < n. Nhập lại!\n")
tp = tuple(range(m, n + 1))
print("Tuple ban đầu:", tp)
mid = len(tp) // 2
tp1 = tp[:mid]
tp2 = tp[mid:]

print("tp1 (nửa đầu):", tp1)
print("tp2 (nửa cuối):", tp2)