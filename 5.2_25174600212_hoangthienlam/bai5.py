import random
A = []
while len(A) < 1000:
    so = random.randint(1, 99999)
    if so % 7 != 0:
        A.append(so)
print("Đã sinh xong 1000 số không chia hết cho 7.")
print("5 số đầu tiên:", A[:5])