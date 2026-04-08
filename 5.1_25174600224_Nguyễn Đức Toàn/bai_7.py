chuoi = input("Nhập chuỗi: ")

i = 0
while i < len(chuoi) and chuoi[i] == " ":
    i += 1
chuoi = chuoi[i:]

i = len(chuoi) - 1
while i >= 0 and chuoi[i] == " ":
    i -= 1
chuoi = chuoi[:i+1]
chuoi_chuan_hoa = ""
trong_khoang = False 

for chuoi_ky_tu in chuoi:
    if chuoi_ky_tu != " ":
        chuoi_chuan_hoa += chuoi_ky_tu
        trong_khoang = False
    else:
        if not trong_khoang:
            chuoi_chuan_hoa += " "
            trong_khoang = True

print("Chuỗi chuẩn hóa:", chuoi_chuan_hoa)