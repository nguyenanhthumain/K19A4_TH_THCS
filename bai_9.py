m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
t = tuple(range(m, n+1))
mid = len(t)//2
tp1 = t[:mid]
tp2 = t[mid:]
print("tp1:", tp1)
print("tp2:", tp2)