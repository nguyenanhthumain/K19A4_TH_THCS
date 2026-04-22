#bai_1
"""
1: Xây dựng hàm không tham số tính lũy thừa bậc n (với n nhập từ bàn phím)
của một số tự nhiên (nhập từ bàn phím)?
"""

a = int(input("Nhập số tự nhiên: "))
n = int(input("Nhập lũy thừa bậc n : "))
def luy_thua(a, n):
    return a ** n
print(f"Lũy thừa bậc {n} của {a} là: {luy_thua(a, n)}")