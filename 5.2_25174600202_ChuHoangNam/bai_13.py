#cau13
chuoi_vao = input("Nhập danh sách mật khẩu: ")
danh_sach_tam = chuoi_vao.split(",")

ket_qua = []

for mk in danh_sach_tam:
    mk = mk.strip() 
    
    n = len(mk)
    if n < 6 or n > 12:
        continue 
        
    chu_thuong = 0
    chu_hoa = 0
    chu_so = 0
    ky_tu_la = 0
    
    for c in mk:
        if 'a' <= c <= 'z':
            chu_thuong += 1
        elif 'A' <= c <= 'Z':
            chu_hoa += 1
        elif '0' <= c <= '9':
            chu_so += 1
        elif c in "$#@ ":
            ky_tu_la += 1
            
    if chu_thuong > 0 and chu_hoa > 0 and chu_so > 0 and ky_tu_la > 0:
        ket_qua.append(mk)

output = ""
for i in range(len(ket_qua)):
    if i == len(ket_qua) - 1:
        output += ket_qua[i]
    else:
        output += ket_qua[i] + ","

print(output)