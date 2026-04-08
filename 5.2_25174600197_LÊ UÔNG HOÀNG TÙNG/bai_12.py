#bai12
mat_khau = input("nhap mat khau: ")
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
if kiem_tra_mat_khau(mat_khau):
    print("mat khau hop le")
else:
    print("mat khau khong hop le")