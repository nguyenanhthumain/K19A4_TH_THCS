# Cách 1 while:
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
while mau == 0:
    print("Mẫu số không được bằng 0!")
    mau = int(input("Nhập lại mẫu số: "))

print("Phân số là:", tu, "/", mau)
# Cách 2 for:
tu = int(input("Nhập tử số: "))
for _ in range(1000):
    mau = int(input("Nhập mẫu số: "))
    if mau != 0:
        break
    print("Mẫu số không được bằng 0!")

print("Phân số là:", tu, "/", mau)
