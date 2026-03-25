# Bài 3:
"""
Viết chương trình nhân 2 số nguyên theo phương pháp Ấn Độ.
"""

a = int(input("Nhập số nguyên dương a : "))
b = int(input("Nhập số nguyên dương b : "))
if a < 0 or b < 0 :
    print("Yêu cầu nhập lại.")
else :
    while a > 0 :
        ab = 0
        if a % 2 == 1 :
            ab = ab + b
        a = a // 2
        b = b * 2
    print("Tích của a và b theo phương pháp Ấn Độ là : ", ab)