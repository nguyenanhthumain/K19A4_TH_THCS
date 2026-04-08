chuoi_nhap = input("Nhập các mật khẩu cách nhau bởi dấu phẩy: ")
danh_sach_tam = chuoi_nhap.split(',')
ket_qua_hop_le = []
for mk in danh_sach_tam:
    mk = mk.strip()
    if 6 <= len(mk) <= 12:
        co_thuong = any('a' <= c <= 'z' for c in mk)
        co_so = any('0' <= c <= '9' for c in mk)
        co_hoa = any('A' <= c <= 'Z' for c in mk)
        co_dac_biet = any(c in "$#@" for c in mk)
        if co_thuong and co_so and co_hoa and co_dac_biet:
            ket_qua_hop_le.append(mk)
print("Các mật khẩu hợp lệ:", ",".join(ket_qua_hop_le))