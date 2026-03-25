"""Bài 1: Viết chương trình để in các số từ n đến n^2, với n là số nguyên dương đượcnhập từ bàn phím."""
n = int(input("Nhập một số nguyên dương: "))
if n > 0:               
    for i in range(n, n**2 + 1):
        print(i, end=' ')  
else:
    print("Vui lòng nhập một số nguyên dương.")