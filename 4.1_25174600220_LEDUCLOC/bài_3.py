"""Bài 3: Viết chương trình nhân 2 số nguyên theo phương pháp Ấn Độ."""

from unittest import result


m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
if m > 0 and n > 0:
    a = 0
    while n > 0:
        if n % 2 == 1:  
            a += m  
        m *= 2  
        n //= 2  
    print("Tích của", m, "và", n, "là:", a)
else:
    print("Vui lòng nhập hai số nguyên dương.")
