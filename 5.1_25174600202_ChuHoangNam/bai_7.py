#cau7
chuoi_vao = input("Nhap chuoi can chuan hoa: ")
danh_sach_tu = chuoi_vao.split()
chuoi_chuan_hoa = ""
for i in range(len(danh_sach_tu)):
    if i == len(danh_sach_tu) - 1:
        chuoi_chuan_hoa += danh_sach_tu[i] 
    else:
        chuoi_chuan_hoa += danh_sach_tu[i] + " "

print("Chuoi sau khi chuan hoa: '" + chuoi_chuan_hoa + "'")