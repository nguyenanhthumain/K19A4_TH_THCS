#cau16
n = int(input("Nhap bac n cua ma tran don vi: "))

A = []
for i in range(n):
    hang = []
    
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
            
    A.append(hang)

print(f"Ma tran don vi bac {n} la:")
for hang in A:
    print(hang)