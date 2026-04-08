#cau6
A = []
seed = 123456789 
for i in range(1000):
    seed = (seed * 1103515245 + 12345) % 99999 + 1
    A.append(seed)

A_cach1 = sorted(A)

A_cach2 = list(A) 
do_dai = len(A_cach2)
for i in range(do_dai):
    for j in range(0, do_dai - i - 1):
        if A_cach2[j] > A_cach2[j + 1]:
            tam = A_cach2[j]
            A_cach2[j] = A_cach2[j + 1]
            A_cach2[j + 1] = tam

print("Da sap xep xong 1000 so bang 2 cach")
print("10 so nho nhat (Cach 2):", A_cach2[:10])