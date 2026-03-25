n = int(input("Nhập giá trị: "))
dau = -1 if n < 0 else 1
so_dao_nguoc = int(str(abs(n))[::-1]) * dau
print(f"Dạng số đảo ngược của số nguyên {n} là:", so_dao_nguoc)
