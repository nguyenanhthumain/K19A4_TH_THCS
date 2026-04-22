#cau1
def tinh_luy_thua():
    a = int(input("Nhap so: "))
    n = int(input("Nhap so mu: "))
    
    ket_qua = 1
    
    for i in range(n):
        ket_qua = ket_qua * a
        
    print("Ket qua:", ket_qua)
tinh_luy_thua()