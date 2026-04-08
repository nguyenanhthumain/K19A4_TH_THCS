n = int(input("Nhập bậc n của ma trận đơn vị: "))
lst_A = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1) 
        else:
            hang.append(0)  
    lst_A.append(hang)
print("Ma trận đơn vị bậc:", n)
for hang in lst_A:
    print(hang,end=" ")