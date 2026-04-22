def tinh_luong(nam):
    return 1500000 + nam * 200000

ten = input("Tên: ")
que = input("Quê: ")
nam = int(input("Thâm niên: "))

print("Tên:", ten)
print("Quê:", que)
print("Lương:", tinh_luong(nam))