mat_khau=input("Nhập mật khẩu: ")

co_chu_thuong=0
co_chu_hoa=0
co_so=0
co_ky_tu=0

for c in mat_khau:
    if "a"<=c<="z":
        co_chu_thuong=1
    elif "A"<=c<="Z":
        co_chu_hoa=1
    elif "0"<=c<="9":
        co_so=1
    elif c in "S#@":
        co_ky_tu=1

if 6<=len(mat_khau)<=12 and co_chu_thuong and co_chu_hoa and co_so and co_ky_tu:
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu không hợp lệ.")