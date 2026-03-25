n = int(input("Nhập số nguyên: "))
so_dao = 0

while n != 0:
    so_dao = so_dao * 10 + n % 10
    n = n // 10

print(so_dao)