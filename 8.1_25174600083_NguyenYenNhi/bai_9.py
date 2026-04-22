#bai_9
"""
Viết chương trình thực hiện các phép tính số học gồm cộng, trừ, nhân và
chia hai số a, b. Tương tự, xây dựng hàm tính luỹ thừa a**(b+n), b**(n+2**a) với n, a được
nhập từ bàn phím.
"""
def tinh(a, b):
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b 
    if b != 0 :
        thuong = a / b
    else:
        thuong = "Không thể chia cho 0"
    return tong, hieu, tich, thuong
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tong, hieu, tich, thuong = tinh(a, b)
print(f"Tổng: {tong}, Hiệu: {hieu}, Tích: {tich}, Thương: {thuong}")

def tinh_luy_thua(a, b, n):
    luy_thua_a = a ** (b + n)
    luy_thua_b = b ** (n + 2 ** a)
    return luy_thua_a, luy_thua_b
n = int(input("Nhập số n: "))
a = float(input("Nhập số a: "))
luy_thua_a, luy_thua_b = tinh_luy_thua(a, b, n)
print(f"Lũy thừa a**(b+n): {luy_thua_a}, Lũy thừa b**(n+2**a): {luy_thua_b}")   
