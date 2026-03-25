tu = int(input("Nhập tử số:"))
for i in range (1000):
    mau = int(input("Nhập mẫu số:"))
    if mau != 0:
        print(f"Phân số : {tu}/{mau}")
        break
    else:
        print(f"Yêu cầu nhập lại")
