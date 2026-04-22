"""Bài 1: Xây dựng hàm không tham số tính lũy thừa bậc n (với n nhập từ bàn phím)
của một số tự nhiên (nhập từ bàn phím)?"""

def tinh_luy_thua():
    n = int(input("Nhập bậc n: "))
    x = int(input("Nhập số tự nhiên: "))
    luy_thua = x ** n
    print(f"{x} lũy thừa {n} là: {luy_thua}")
tinh_luy_thua()