n = int(input("Nhap so nguyen: "))
so_dao = 0

while n > 0:
    chu_so = n % 10
    so_dao = so_dao * 10 + chu_so
    n = n // 10

print(f"So dao nguoc = {so_dao}")