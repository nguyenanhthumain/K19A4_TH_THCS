#bai6
import random
a = [random.randint(1, 99999) for _ in range(1000)]
print("list truoc khi sap xep (10 so dau):", a[:10])
tang1 = sorted(a)
print("sap xep tang dan dung sorted() (10 so dau):", tang1[:10])
tang2 = a[:]
for i in range(len(tang2)):
    for j in range(i+1, len(tang2)):
        if tang2[i] > tang2[j]:
            tang2[i], tang2[j] = tang2[j], tang2[i]
print("sap xep tang dan khong dung sorted() (10 so dau):", tang2[:10])