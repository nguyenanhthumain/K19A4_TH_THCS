so = input("Nhập một số nguyên: ")
if so[0] == '-':
    dao_nguoc = str(-int(so[1:][::-1]))
else:
    dao_nguoc = str(int(so[::-1]))
 
print(f"Số đảo ngược: {dao_nguoc}")