# Bài 6:
"""
Viết chương trình kiểm tra một số n nhập từ bàn phím có là số nguyên tố không.
"""

n = int(input("Nhập một số nguyên dương n : "))
if n < 2 :  
    print("Yêu cầu nhập lại.")
else :
    for i in range(2, n) :
        if n % i == 0 :
            print(n , "không phải là số nguyên tố.")
            break
    else :
        print(n , "là số nguyên tố.")