n = int(input("Nhập số nguyên: "))
so_dao = 0
tam = abs(n)
while tam > 0:
    chu_so = tam % 10
    so_dao = so_dao * 10 + chu_so
    tam //= 10
if n < 0:
    so_dao = -so_dao
print("Số đaor ngược là:", so_dao)