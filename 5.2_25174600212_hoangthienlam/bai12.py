import re

def kiem_tra_mat_khau(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password): 
        return False
    return True
chuoi_nhap = input("Nhập các mật khẩu cách nhau bởi dấu phẩy: ")
danh_sach_mk = chuoi_nhap.split(",")
ket_qua = []
for mk in danh_sach_mk:
    mk = mk.strip() 
    if kiem_tra_mat_khau(mk):
        ket_qua.append(mk)
print(",".join(ket_qua))