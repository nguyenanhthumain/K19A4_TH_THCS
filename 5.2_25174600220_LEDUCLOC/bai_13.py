"""13. Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy
và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ
sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy. Ví dụ nếu mật khẩu nhập vào
chương trình là: ABd1234@1, a FI#,2w3E*, 2We3345 thì đầu ra sẽ là:
ABd1234@1."""

chuoi_mat_khau = input("Nhập mật khẩu: ")

danh_sach_mk = chuoi_mat_khau.split(",")
ket_qua = []

for mk in danh_sach_mk:
    mk = mk.strip()
    
    if 6 <= len(mk) <= 12:
        co_chu_thuong = False
        co_chu_hoa = False
        co_so = False
        co_ky_tu_db = False
        
        for ky_tu in mk:
            if 'a' <= ky_tu <= 'z':
                co_chu_thuong = True
            elif 'A' <= ky_tu <= 'Z':
                co_chu_hoa = True
            elif '0' <= ky_tu <= '9':
                co_so = True
            elif ky_tu in "$#@":
                co_ky_tu_db = True
        
        if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_db:
            ket_qua.append(mk)

print(",".join(ket_qua))