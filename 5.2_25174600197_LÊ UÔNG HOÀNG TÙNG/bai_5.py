#bai5
import random
a = []
while len(a) < 1000:
    so = random.randint(1, 99999)
    if so % 7 != 0:
        a.append(so)
print("da sinh xong list 1000 so khong chia het cho 7")
print("10 so dau tien:", a[:10])