tu_so = int(input("Nhập tử số: "))

print("CÁCH 1:FOR")
for _ in range(100):
    mau_so_for = int(input("Nhập mẫu số (khác 0): "))
    if mau_so_for != 0:
        print(f"-> Phân số hợp lệ (FOR): {tu_so}/{mau_so_for}")
        break
    print("Lỗi: Mẫu số bằng 0. Nhập lại!")

print("CÁCH 2:WHILE")
while True:
    mau_so_while = int(input("Nhập mẫu số (khác 0): "))
    if mau_so_while != 0:
        print(f"-> Phân số hợp lệ (WHILE): {tu_so}/{mau_so_while}")
        break
    print("Lỗi: Mẫu số bằng 0. Nhập lại!")