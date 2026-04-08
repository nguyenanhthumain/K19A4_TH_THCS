#bai_12
"""
Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký.
Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
Các tiêu chí kiểm tra mật khẩu bao gồm thỏa mãn đầy đủ các yêu cầu sau:
a. Ít nhất 1 chữ cái nằm trong [a-z]
b. Ít nhất 1 số nằm trong [0-9].
c. Ít nhất 1 kí tự nằm trong [A-Z]
d. Ít nhất 1 ký tự nằm trong [S# @].
e. Độ dài mật khẩu tối thiểu: 6 ký tự.
f. Độ dài mật khẩu tối đa: 12 ký tự.
"""

mk = input("Nhập mật khẩu: ")
if (len(mk) < 6 or len(mk) > 12):
    print("Mật khẩu phải có độ dài từ 6 đến 12 ký tự.")

ket_qua = []
danh_sach_pass = mk.split(",") 

for i in danh_sach_pass:
    password = i.strip()
    chu_thuong = False
    chu_hoa = False
    so = False
    ky_tu_db = False
    
    
    for mk_pass in password:
        if 'a' <= mk_pass <= 'z':
            chu_thuong = True
        elif 'A' <= mk_pass <= 'Z':
            chu_hoa = True
        elif '0' <= mk_pass <= '9':
            so = True
        elif mk_pass in "$#@ ": 
            ky_tu_db = True
    if chu_thuong and chu_hoa and so and ky_tu_db:
        ket_qua.append(password)
print(",".join(ket_qua))