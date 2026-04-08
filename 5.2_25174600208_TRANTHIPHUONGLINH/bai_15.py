X=int(input("Nhập X: "))
Y=int(input("Nhập Y: "))
mat=[]
for i in range(X):
    row=[]
    for j in range(Y):
        row.append(i*j)
    mat.append(row)
print("Ma trận 2 chiều:")
for r in mat:
    print(r)