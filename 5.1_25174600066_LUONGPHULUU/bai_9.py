m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
lst = []
for i in range(m, n + 1):
    lst.append(i)
tp = tuple(lst)
print("Tuple ban đầu:", tp)
mid = len(tp) // 2
tp1 = tp[:mid]
tp2 = tp[mid:]
print("Tuple nửa đầu (tp1):", tp1)
print("Tuple nửa cuối (tp2):", tp2)