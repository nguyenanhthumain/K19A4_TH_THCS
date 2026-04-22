#bai_12
"""
12: Viết chương trình tính lương của nhân viên:
+ Viết hàm nhập họ tên, quê quán, thâm niên công tác của một nhân viên.
+ Viết hàm tính lương dựa vào thâm niên công tác.
+ Việt hàm xuất họ tên, quê quán, thâm niên công tác và lương của nhân viên.
+ Viết chương trình nhập thông tin của nhân viên, tính lương và xuất thông tin
của nhân viên (kể cả lương) ra màn hình bằng cách sử dụng ba hàm trên.
"""
def nhap_thong_tin():
    ho_ten = input("Nhập họ tên : ")
    que_quan = input("Nhập quê quán : ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ho_ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    if tham_nien < 5:
        luong = 5000000
    elif tham_nien < 10:
        luong = 7000000
    else:
        luong = 10000000
    return luong
def xuat_thong_tin(ho_ten, que_quan, tham_nien, luong):
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên công tác: {tham_nien} năm")
    print(f"Lương: {luong} VND")
ho_ten, que_quan, tham_nien = nhap_thong_tin()
luong = tinh_luong(tham_nien)   
xuat_thong_tin(ho_ten, que_quan, tham_nien, luong)
