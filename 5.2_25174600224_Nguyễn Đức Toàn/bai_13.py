chuoi=input("Nhập mật khẩu: ")
danh_sach_mat_khau=[x.strip() for x in chuoi.split(",")]

danh_sach_hop_le=[]

for mat_khau in danh_sach_mat_khau:
    co_chu_thuong=0
    co_chu_hoa=0
    co_so=0
    co_ky_tu=0
    
    for ky_tu in mat_khau:
        if "a"<=ky_tu<="z":
            co_chu_thuong=1
        elif "A"<=ky_tu<="Z":
            co_chu_hoa=1
        elif "0"<=ky_tu<="9":
            co_so=1
        elif ky_tu in "S#@":
            co_ky_tu=1

    if 6<=len(mat_khau)<=12 and co_chu_thuong and co_chu_hoa and co_so and co_ky_tu:
        danh_sach_hop_le=danh_sach_hop_le+[mat_khau]

for i in range(len(danh_sach_hop_le)):
    if i==len(danh_sach_hop_le)-1:
        print(danh_sach_hop_le[i])
    else:
        print(danh_sach_hop_le[i], end=", ")