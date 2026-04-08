#bai13
chuoi = input("nhap cac mat khau cach nhau boi dau phay: ")
mat_khau_list = [mk.strip() for mk in chuoi.split(',')]
def kiem_tra_mat_khau(mk):
    if len(mk) < 6 or len(mk) > 12:
        return False
    if not any(c.islower() for c in mk):
        return False
    if not any(c.isupper() for c in mk):
        return False
    if not any(c.isdigit() for c in mk):
        return False
    if not any(c in "$#@ " for c in mk):
        return False
    return True
ket_qua = [mk for mk in mat_khau_list if kiem_tra_mat_khau(mk)]
print("mat khau hop le:", ', '.join(ket_qua))