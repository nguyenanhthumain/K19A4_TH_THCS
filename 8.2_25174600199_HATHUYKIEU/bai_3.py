import random
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n: "))
ds = []
for i in range(n):
    ds.append(random.randint(1, 50))
print("Danh sách:", ds)
print("Các số nguyên tố trong danh sách là:")
for x in ds:
    if la_so_nguyen_to(x):
        print(x, end=" ")