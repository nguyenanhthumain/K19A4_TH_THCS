m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
 
if m < n:
    m, n = n, m
 
while n != 0:
    r = m % n
    m = n
    n = r
 
print(f"UCLN = {m}")