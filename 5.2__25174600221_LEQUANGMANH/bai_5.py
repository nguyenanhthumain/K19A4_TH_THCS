import random
A = []
while len(A) < 1000:
    num = random.randint(1, 99999)
    if num % 7 != 0:
        A.append(num)
print("5. Đã sinh 1000 số không chia hết cho 7. 10 số đầu:", A[:10])