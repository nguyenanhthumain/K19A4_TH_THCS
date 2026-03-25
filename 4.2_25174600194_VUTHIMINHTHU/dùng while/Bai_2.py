tu = int(input("Nhập tử số:"))
while True:
    mau = int(input("Nhập mẫu số: "))
    if mau != 0:
        break
    else:
        print(f"Yêu cầu nhập lại")
print(f"Phân số là: {tu}/{mau}")
