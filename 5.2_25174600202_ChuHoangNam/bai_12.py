#cau12
password = input("Nhap mat khau de dang ky: ")

co_chu_thuong = False
co_chu_hoa = False
co_chu_so = False
co_ky_tu_dac_biet = False

ky_tu_dac_biet = "$#@ " 

do_dai = len(password)
if 6 <= do_dai <= 12:
    
    for char in password:
        if char.islower():
            co_chu_thuong = True
        elif char.isupper():
            co_chu_hoa = True
        elif char.isdigit():
            co_chu_so = True
        elif char.find(ky_tu_dac_biet) != -1: 
            co_ky_tu_dac_biet = True

    if co_chu_thuong and co_chu_hoa and co_chu_so and co_ky_tu_dac_biet:
        print("Mat khau hop le!")
    else:
        print("Mat khau khong hop le. Vui long kiem tra lai cac ky tu.")
else:
    print("Mat khau khong hop le. Do dai phai tu 6 den 12 ky tu.")