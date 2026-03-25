tu_so = int(input("Nhap vao tu so: "))

# While
mau_so = 0
while True:
    mau_so = int(input("Nhap vao mau so (khac 0): "))
    if mau_so != 0:
        break
    print("Loi: Mau so khong the bang 0!")

# For
for _ in range(1):
    print(f"Phan so ban vua nhap la: {tu_so}/{mau_so}")