def nhap_nv():
    name = input("Họ tên: ")
    que = input("Quê quán: ")
    years = int(input("Thâm niên: "))
    return name, que, years

def tinh_luong(years):
    return 3000000 + years * 500000

def xuat_nv(name, que, years, salary):
    print("Tên:", name)
    print("Quê:", que)
    print("Thâm niên:", years)
    print("Lương:", salary)

# chạy
name, que, years = nhap_nv()
salary = tinh_luong(years)
xuat_nv(name, que, years, salary)