A = []
x = 1  
while len(A) < 1000:
    x = (1103515245 * x + 12345) % (2**31)
    num = x % 99999 + 1
    if num % 7 != 0:
        A.append(num)
print("Số phần tử:", len(A))
print("10 phần tử đầu:", A[:10])