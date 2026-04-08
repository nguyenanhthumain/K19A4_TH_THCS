import random

a = []
for i in range(0, 201):
    if i % 5 == 0 and i % 7 == 0:
        a.append(i)
vt = random.randint(0, len(a)-1)
print("Số ngẫu nhiên chia hết 5 và 7:", a[vt])