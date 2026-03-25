# Bài 1:
"""
Viết chương trình để in các số từ n đến n 2 , với n là số nguyên dương được nhập từ bàn phím.
"""

n = int(input("Nhập một số nguyên dương n : "))
if n < 0 :
    print("Yêu cầu nhập lại.")
else :
    for i in range(n, n**2 + 1):
        print(i, end=' ')