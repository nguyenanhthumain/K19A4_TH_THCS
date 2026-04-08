"""12. Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký.
Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
Các tiêu chí kiểm tra mật khẩu bao gồm thỏa mãn đầy đủ các yêu cầu sau:
a. Ít nhất 1 chữ cái nằm trong [a-z]
b. Ít nhất 1 số nằm trong [0-9].
c. Ít nhất 1 kí tự nằm trong [A-Z]
d. Ít nhất 1 ký tự nằm trong [S# @].
e. Độ dài mật khẩu tối thiểu: 6 ký tự.
f. Độ dài mật khẩu tối đa: 12 ký tự."""

mat_khau = input("Nhập mật khẩu cần kiểm tra: ")

if 6 <= len(mat_khau) <= 12:
    co_chu_thuong = False 
    co_so = False         
    co_chu_hoa = False    
    co_ky_tu_db = False   

    for chu in mat_khau:
        if 'a' <= chu <= 'z':
            co_chu_thuong = True
        elif '0' <= chu <= '9':
            co_so = True
        elif 'A' <= chu <= 'Z':
            co_chu_hoa = True
        elif chu in "$# @":
            co_ky_tu_db = True
    
    if co_chu_thuong and co_so and co_chu_hoa and co_ky_tu_db:
        print("Mật khẩu hợp lệ!")
    else:
        print("Mật khẩu KHÔNG hợp lệ (Thiếu loại ký tự bắt buộc).")
        if not co_chu_thuong: print("- Thiếu chữ thường")
        if not co_chu_hoa:    print("- Thiếu chữ hoa")
        if not co_so:         print("- Thiếu số")
        if not co_ky_tu_db:   print("- Thiếu ký tự đặc biệt ($# @)")
else:
    print("Mật khẩu KHÔNG hợp lệ (Độ dài phải từ 6-12 ký tự).")