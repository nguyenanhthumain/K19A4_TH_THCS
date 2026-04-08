#bai11
n = int(input("nhap n: "))
a = [int(input(f"nhap so thu {i+1}: ")) for i in range(n)]
b = [x for x in a if x % 3 == 0 and x % 5 != 0]
c = [x**2 for x in a]
d = [any.choice([x for x in a if x % 3 == 0]) for _ in range(5)] if any(x % 3 == 0 for x in a) else []
print("danh sach b:", b)
print("danh sach c:", c)
print("danh sach d:", d)