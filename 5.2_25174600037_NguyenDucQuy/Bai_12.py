mat_khau = input("Nhập mật khẩu cần kiểm tra: ")
co_chu_thuong = False
co_so = False
co_chu_hoa = False
co_ky_tu_dac_biet = False
if 6 <= len(mat_khau) <= 12:
    for ky_tu in mat_khau:
        if 'a' <= ky_tu <= 'z': co_chu_thuong = True
        elif '0' <= ky_tu <= '9': co_so = True
        elif 'A' <= ky_tu <= 'Z': co_chu_hoa = True
        elif ky_tu in "$#@": co_ky_tu_dac_biet = True
if co_chu_thuong and co_so and co_chu_hoa and co_ky_tu_dac_biet:
    print("Mật khẩu hợp lệ!")
else:
    print("Mật khẩu không hợp lệ.")