#WHILE
tu_so = int(input("Nhập tử số: "))
mau_so = 0

while mau_so == 0:
    mau_so = int(input("Nhập mẫu số (khác 0): "))
    if mau_so == 0:
        print("Mẫu số không thể bằng 0. Hãy nhập lại!")

print(f"Phân số vừa nhập: {tu_so}/{mau_so}")



# FOR
tu_so = int(input("Nhập tử số: "))

for i in range(1000):
    n = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break 
    else:
        print("Mẫu số phải khác 0. Vui lòng nhập lại!")

print(f"Phân số bạn vừa nhập là: {tu_so}/{mau_so}")