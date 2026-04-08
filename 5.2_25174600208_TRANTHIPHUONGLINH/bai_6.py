A=[]
for i in range(1,1001):
    A.append(i)
print("Gốc:",A)

#sắpxếp tăng
B=A.copy()
for i in range(len(B)):
    for j in range(len(B)-i-1):
        if B[j]>B[j+1]:
            B[j],B[j+1]=B[j+1],B[j]
print("Tăng:",B)